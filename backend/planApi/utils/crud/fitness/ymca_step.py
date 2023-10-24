from core.models import User
from django.forms import ValidationError
from planApi.models.fitness_models import YMCAStepAssessments, YMCAStepTest
from planApi.utils.serializers.fitness import (
    YMCAStepAssessmentsSerializer,
    YMCAStepTestSerializer,
)
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response


def get_ymca_step_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = YMCAStepAssessments.objects.filter(trainee=user)
    serializer = YMCAStepAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_ymca_step_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = YMCAStepAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_ymca_step_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(YMCAStepTest, id=test_id)
    serializer = YMCAStepTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_ymca_step_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_ymca_step_test)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_assessment = YMCAStepAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            test = YMCAStepTest(
                assessment=new_assessment,
                recovery_hr=float(data[0][i]),
                rating=data[1][i],
            )

            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_ymca_step_test(request, test_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_ymca_step_test)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        test_queryset = YMCAStepTest.objects.filter(id=test_id)
        if not test_queryset.exists():
            return Response(
                {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
            )
        test_instance = test_queryset.first()

        for i in range(len(data[0])):
            try:
                test_instance.recovery_hr = float(data[0][i])
                test_instance.rating = data[1][i]
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


def delete_ymca_step_test(request, test_id):
    test = YMCAStepTest.objects.filter(id=test_id)
    test.delete()

    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
