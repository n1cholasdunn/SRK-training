from core.models import User
from django.forms import ValidationError
from google_sheets.utils.getters.get_fitness_assessments import get_overhead_squat
from planApi.models.fitness_models import OverheadSquatAssessments, OverheadSquatTest
from planApi.utils.fitness_serializers import (
    OverheadSquatAssessmentsSerializer,
    OverheadSquatTestSerializer,
)
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response


def get_overhead_squat_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = OverheadSquatAssessments.objects.filter(trainee=user)
    serializer = OverheadSquatAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_overhead_squat_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = OverheadSquatAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_overhead_squat_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(OverheadSquatTest, id=test_id)
    serializer = OverheadSquatTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_overhead_squat_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_overhead_squat)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_assessment = OverheadSquatAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            test = OverheadSquatTest(
                assessment=new_assessment,
                foot_ankle=data[0][i],
                knee=data[1][i],
                # TODO test lphc to see if inputs properly formatted
                lphc=data[2][i] + " " + data[3][i],
                shoulder=data[4][i],
                solutions=data[5][i],
            )

            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_overhead_squat_test(request, test_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_overhead_squat)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        test_queryset = OverheadSquatTest.objects.filter(id=test_id)
        if not test_queryset.exists():
            return Response(
                {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
            )
        test_instance = test_queryset.first()

        for i in range(len(data[0])):
            try:
                test_instance.foot_ankle = data[0][i]
                test_instance.knee = data[1][i]
                # TODO test lphc to see if inputs properly formatted
                test_instance.lphc = data[2][i] + " " + data[3][i]
                test_instance.shoulder = data[4][i]
                test_instance.solutions = data[5][i]
                test_instance.save()
            except (
                ValidationError,
            ) as e:  # ValidationError in case there's any issue during saving.
                return Response(
                    {"error": f"Invalid data: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def delete_overhead_squat_test(request, test_id):
    test = OverheadSquatTest.objects.filter(id=test_id)
    test.delete()

    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
