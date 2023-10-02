import requests
from decimal import Decimal, InvalidOperation
from rest_framework.response import Response
from rest_framework import status
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


def get_health_markers_assessments(request, test_id):
    tests = HealthMarkersTest.objects.filter(id=test_id)
    serializer = HealthMarkersAssessmentsSerializer(tests, many=True)
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
                print("Converting:", data[5][i], type(data[5][i]))
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
