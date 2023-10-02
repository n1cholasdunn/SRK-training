from core.models import User
import requests
from decimal import Decimal, InvalidOperation
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.gsheets.getters.get_fitness_assessments import (
    get_core_strength,
    get_davies,
    get_overhead_squat,
    get_pushups,
    get_sharks_skills,
    get_sit_reach,
    get_ymca_step_test,
    get_health_markers,
    get_measurements,
)
from ..models.fitness_models import (
    HealthMarkersAssessments,
    HealthMarkersTest,
    MeasurementsAssessments,
    MeasurementsTest,
    OverheadSquatAssessments,
    OverheadSquatTest,
    YMCAStepAssessments,
    YMCAStepTest,
    SitReachAssessments,
    SitReachTest,
    PushUpAssessments,
    PushUpTest,
    DaviesAssessments,
    DaviesTest,
    SharkSkillsAssessments,
    SharkSkillsTest,
    SharkSkillsSide,
    CoreAssessments,
    CoreTest,
)
from ..serializers import (
    HealthMarkersAssessmentsSerializer,
    HealthMarkersTestSerializer,
    MeasurementsAssessmentsSerializer,
    MeasurementsTestSerializer,
    OverheadSquatAssessmentsSerializer,
    OverheadSquatTestSerializer,
    YMCAStepAssessmentsSerializer,
    YMCAStepTestSerializer,
    SitReachAssessmentsSerializer,
    SitReachTestSerializer,
    PushUpAssessmentsSerializer,
    PushUpTestSerializer,
    DaviesAssessmentsSerializer,
    DaviesTestSerializer,
    SharkSkillsAssessmentsSerializer,
    SharkSkillsTestSerializer,
    SharkSkillsSideSerializer,
    CoreAssessmentsSerializer,
    CoreTestSerializer,
)


#!Health Markers
def get_health_markers_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(HealthMarkersTest, id=test_id)
    serializer = HealthMarkersTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_health_markers_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = HealthMarkersAssessments.objects.filter(trainee=user)
    serializer = HealthMarkersAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_health_markers_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_health_markers)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_assessment = HealthMarkersAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            try:
                weight = Decimal(data[0][i])
                bmi = Decimal(data[1][i])
                waist_hip_ratio = Decimal(data[2][i])
                resting_hr = Decimal(data[3][i])
                blood_pressure = data[4][i]
                vo2_max = Decimal(data[5][i])
            except InvalidOperation as e:
                return Response(
                    {"error": f"Invalid number format: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            test = HealthMarkersTest(
                assessment=new_assessment,
                weight=weight,
                bmi=bmi,
                waist_hip_ratio=waist_hip_ratio,
                resting_hr=resting_hr,
                blood_pressure=blood_pressure,
                vo2_max=vo2_max,
            )

            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_health_markers_test(request, test_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_health_markers)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        test_queryset = HealthMarkersTest.objects.filter(id=test_id)
        if not test_queryset.exists():
            return Response(
                {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
            )
        test_instance = test_queryset.first()

        for i in range(len(data[0])):
            try:
                test_instance.weight = Decimal(data[0][i])
                test_instance.bmi = Decimal(data[1][i])
                test_instance.waist_hip_ratio = Decimal(data[2][i])
                test_instance.resting_hr = Decimal(data[3][i])
                test_instance.blood_pressure = data[4][i]
                test_instance.vo2_max = Decimal(data[5][i])
                test_instance.save()
            except (
                InvalidOperation,
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


def delete_health_markers_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = HealthMarkersAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


#!Measurements
def get_measurements_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(MeasurementsTest, id=test_id)
    serializer = MeasurementsTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_measurements_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = MeasurementsAssessments.objects.filter(trainee=user)
    serializer = MeasurementsAssessmentsSerializer(assessments, many=True)
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
                chest = Decimal(data[0][i])
                biceps = Decimal(data[1][i])
                forearms = Decimal(data[2][i])
                lower_abdomen = Decimal(data[3][i])
                hips = Decimal(data[4][i])
                upper_thigh = Decimal(data[5][i])
                mid_thigh = Decimal(data[6][i])
                calves = Decimal(data[7][i])
            except InvalidOperation as e:
                return Response(
                    {"error": f"Invalid number format: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            test = MeasurementsTest(
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
    test = get_object_or_404(MeasurementsTest, id=test_id)
    serializer = MeasurementsTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
                test_instance.chest = Decimal(data[0][i])
                test_instance.biceps = Decimal(data[1][i])
                test_instance.forearms = Decimal(data[2][i])
                test_instance.lower_abdomen = Decimal(data[3][i])
                test_instance.hips = Decimal(data[4][i])
                test_instance.upper_thigh = Decimal(data[5][i])
                test_instance.mid_thigh = Decimal(data[6][i])
                test_instance.calves = Decimal(data[7][i])
                test_instance.save()
            except (
                InvalidOperation,
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
