from core.models import User
from django.forms import ValidationError
from google_sheets.utils.getters.get_fitness_assessments import get_measurements
from common.models.fitness_models import MeasurementsAssessments, MeasurementsTest
from common.utils.fitness_serializers import (
    MeasurementsAssessmentsSerializer,
    MeasurementsTestSerializer,
)
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response


def get_measurements_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = MeasurementsAssessments.objects.filter(trainee=user)
    serializer = MeasurementsAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_measurements_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = MeasurementsAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_measurements_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(MeasurementsTest, id=test_id)
    serializer = MeasurementsTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_measurements_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_measurements)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_assessment = MeasurementsAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            try:
                chest = float(data[0][i])
                biceps = float(data[1][i])
                forearms = float(data[2][i])
                lower_abdomen = float(data[3][i])
                hips = float(data[4][i])
                upper_thigh = float(data[5][i])
                mid_thigh = float(data[6][i])
                calves = float(data[7][i])
            except ValidationError as e:
                return Response(
                    {"error": f"Invalid form: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            test = MeasurementsTest(
                assessment=new_assessment,
                chest=chest,
                biceps=biceps,
                forearms=forearms,
                lower_abdomen=lower_abdomen,
                hips=hips,
                upper_thigh=upper_thigh,
                mid_thigh=mid_thigh,
                calves=calves,
            )

            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_measurements_test(request, test_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_measurements)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        test_queryset = MeasurementsTest.objects.filter(id=test_id)
        if not test_queryset.exists():
            return Response(
                {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
            )
        test_instance = test_queryset.first()

        for i in range(len(data[0])):
            try:
                test_instance.chest = float(data[0][i])
                test_instance.biceps = float(data[1][i])
                test_instance.forearms = float(data[2][i])
                test_instance.lower_abdomen = float(data[3][i])
                test_instance.hips = float(data[4][i])
                test_instance.upper_thigh = float(data[5][i])
                test_instance.mid_thigh = float(data[6][i])
                test_instance.calves = float(data[7][i])
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


def delete_measurements_test(request, test_id):
    test = MeasurementsTest.objects.filter(id=test_id)
    test.delete()

    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
