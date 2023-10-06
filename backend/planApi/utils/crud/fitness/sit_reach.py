from core.models import User
from django.forms import ValidationError
from planApi.gsheets.getters.get_fitness_assessments import get_sit_reach
from planApi.models.fitness_models import SitReachAssessments, SitReachTest
from planApi.serializers import SitReachAssessmentsSerializer, SitReachTestSerializer
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response

def get_sit_reach_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = SitReachAssessments.objects.filter(trainee=user)
    serializer = SitReachAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_sit_reach_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = SitReachAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_sit_reach_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(SitReachTest, id=test_id)
    serializer = SitReachTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_sit_reach_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_sit_reach)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_assessment = SitReachAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            test = SitReachTest(
                assessment=new_assessment,
                first_measurement=float(data[0][i]),
                second_measurement=float(data[1][i]),
                third_measurement=float(data[2][i]),
            )

            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_sit_reach_test(request, test_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_sit_reach)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        test_queryset = SitReachTest.objects.filter(id=test_id)
        if not test_queryset.exists():
            return Response(
                {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
            )
        test_instance = test_queryset.first()

        for i in range(len(data[0])):
            try:
                test_instance.first_measurement = float(data[0][i])
                test_instance.second_measurement = float(data[1][i])
                test_instance.third_measurement = float(data[2][i])
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


def delete_sit_reach_test(request, test_id):
    test = SitReachTest.objects.filter(id=test_id)
    test.delete()

    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )