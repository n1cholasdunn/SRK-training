from core.models import User
import requests
from decimal import Decimal, InvalidOperation
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.gsheets.getters.get_fitness_assessments import (
    get_core,
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


# TODO extract functions to new folder per type of test/assessment
# #!Health Markers
# def get_health_markers_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = HealthMarkersAssessments.objects.filter(trainee=user)
#     serializer = HealthMarkersAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_health_markers_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = HealthMarkersAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_health_markers_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(HealthMarkersTest, id=test_id)
#     serializer = HealthMarkersTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_health_markers_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_health_markers)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = HealthMarkersAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             try:
#                 weight = Decimal(data[0][i])
#                 bmi = Decimal(data[1][i])
#                 waist_hip_ratio = Decimal(data[2][i])
#                 resting_hr = Decimal(data[3][i])
#                 blood_pressure = data[4][i]
#                 vo2_max = Decimal(data[5][i])
#             except InvalidOperation as e:
#                 return Response(
#                     {"error": f"Invalid number format: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             test = HealthMarkersTest(
#                 assessment=new_assessment,
#                 weight=weight,
#                 bmi=bmi,
#                 waist_hip_ratio=waist_hip_ratio,
#                 resting_hr=resting_hr,
#                 blood_pressure=blood_pressure,
#                 vo2_max=vo2_max,
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_health_markers_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_health_markers)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = HealthMarkersTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.weight = Decimal(data[0][i])
#                 test_instance.bmi = Decimal(data[1][i])
#                 test_instance.waist_hip_ratio = Decimal(data[2][i])
#                 test_instance.resting_hr = Decimal(data[3][i])
#                 test_instance.blood_pressure = data[4][i]
#                 test_instance.vo2_max = Decimal(data[5][i])
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_health_markers_test(request, test_id):
#     test = HealthMarkersTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Measurements
# def get_measurements_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = MeasurementsAssessments.objects.filter(trainee=user)
#     serializer = MeasurementsAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_measurements_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = MeasurementsAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_measurements_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(MeasurementsTest, id=test_id)
#     serializer = MeasurementsTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_measurements_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_measurements)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = MeasurementsAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             try:
#                 chest = Decimal(data[0][i])
#                 biceps = Decimal(data[1][i])
#                 forearms = Decimal(data[2][i])
#                 lower_abdomen = Decimal(data[3][i])
#                 hips = Decimal(data[4][i])
#                 upper_thigh = Decimal(data[5][i])
#                 mid_thigh = Decimal(data[6][i])
#                 calves = Decimal(data[7][i])
#             except InvalidOperation as e:
#                 return Response(
#                     {"error": f"Invalid number format: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             test = MeasurementsTest(
#                 assessment=new_assessment,
#                 chest=chest,
#                 biceps=biceps,
#                 forearms=forearms,
#                 lower_abdomen=lower_abdomen,
#                 hips=hips,
#                 upper_thigh=upper_thigh,
#                 mid_thigh=mid_thigh,
#                 calves=calves,
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_measurements_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_measurements)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = MeasurementsTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.chest = Decimal(data[0][i])
#                 test_instance.biceps = Decimal(data[1][i])
#                 test_instance.forearms = Decimal(data[2][i])
#                 test_instance.lower_abdomen = Decimal(data[3][i])
#                 test_instance.hips = Decimal(data[4][i])
#                 test_instance.upper_thigh = Decimal(data[5][i])
#                 test_instance.mid_thigh = Decimal(data[6][i])
#                 test_instance.calves = Decimal(data[7][i])
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_measurements_test(request, test_id):
#     test = MeasurementsTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Overhead Squat
# def get_overhead_squat_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = OverheadSquatAssessments.objects.filter(trainee=user)
#     serializer = OverheadSquatAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_overhead_squat_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = OverheadSquatAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_overhead_squat_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(OverheadSquatTest, id=test_id)
#     serializer = OverheadSquatTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_overhead_squat_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_overhead_squat)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = OverheadSquatAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = OverheadSquatTest(
#                 assessment=new_assessment,
#                 foot_ankle=data[0][i],
#                 knee=data[1][i],
#                 # TODO test lphc to see if inputs properly formatted
#                 lphc=data[2][i] + " " + data[3][i],
#                 shoulder=data[4][i],
#                 solutions=data[5][i],
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_overhead_squat_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_overhead_squat)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = OverheadSquatTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.foot_ankle = data[0][i]
#                 test_instance.knee = data[1][i]
#                 # TODO test lphc to see if inputs properly formatted
#                 test_instance.lphc = data[2][i] + " " + data[3][i]
#                 test_instance.shoulder = data[4][i]
#                 test_instance.solutions = data[5][i]
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_overhead_squat_test(request, test_id):
#     test = OverheadSquatTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!YMCA Step Test
# def get_ymca_step_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = YMCAStepAssessments.objects.filter(trainee=user)
#     serializer = YMCAStepAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_ymca_step_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = YMCAStepAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_ymca_step_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(YMCAStepTest, id=test_id)
#     serializer = YMCAStepTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_ymca_step_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_ymca_step_test)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = YMCAStepAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = YMCAStepTest(
#                 assessment=new_assessment,
#                 recovery_hr=Decimal(data[0][i]),
#                 rating=data[1][i],
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_ymca_step_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_ymca_step_test)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = YMCAStepTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.recovery_hr = Decimal(data[0][i])
#                 test_instance.rating = data[1][i]
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_ymca_step_test(request, test_id):
#     test = YMCAStepTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Sit & Reach
# def get_sit_reach_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = SitReachAssessments.objects.filter(trainee=user)
#     serializer = SitReachAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_sit_reach_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = SitReachAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_sit_reach_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(SitReachTest, id=test_id)
#     serializer = SitReachTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_sit_reach_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_sit_reach)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = SitReachAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = SitReachTest(
#                 assessment=new_assessment,
#                 first_measurement=Decimal(data[0][i]),
#                 second_measurement=Decimal(data[1][i]),
#                 third_measurement=Decimal(data[2][i]),
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_sit_reach_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_sit_reach)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = SitReachTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.first_measurement = Decimal(data[0][i])
#                 test_instance.second_measurement = Decimal(data[1][i])
#                 test_instance.third_measurement = Decimal(data[2][i])
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_sit_reach_test(request, test_id):
#     test = SitReachTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Pushups
# def get_pushup_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = PushUpAssessments.objects.filter(trainee=user)
#     serializer = PushUpAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_pushup_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = PushUpAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_pushup_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(PushUpTest, id=test_id)
#     serializer = PushUpTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_pushup_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_pushups)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = PushUpAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = PushUpTest(
#                 assessment=new_assessment,
#                 num_pushups=int(data[0][i]),
#                 completed=True if data[1][i].upper() == "Y" else False,
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_pushup_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_pushups)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = PushUpTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.num_pushups = int(data[0][i])
#                 test_instance.completed = True if data[1][i].upper() == "Y" else False
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_pushup_test(request, test_id):
#     test = PushUpTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Davies Test
# def get_davies_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = DaviesAssessments.objects.filter(trainee=user)
#     serializer = DaviesAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_davies_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = DaviesAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_davies_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(DaviesTest, id=test_id)
#     serializer = DaviesTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_davies_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_davies)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = DaviesAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = DaviesTest(
#                 assessment=new_assessment,
#                 first_trial=int(data[0][i]),
#                 second_trial=int(data[1][i]),
#                 third_trial=int(data[2][i]),
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_davies_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_davies)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = DaviesTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()
#         for i in range(len(data[0])):
#             try:
#                 test_instance.first_trial = int(data[0][i])
#                 test_instance.second_trial = int(data[1][i])
#                 test_instance.third_trial = int(data[2][i])
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_davies_test(request, test_id):
#     test = DaviesTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Core Test
# def get_core_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = CoreAssessments.objects.filter(trainee=user)
#     serializer = CoreAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_core_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = CoreAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def get_core_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(CoreTest, id=test_id)
#     serializer = CoreTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def input_core_test(request):
#     if request.method == "POST":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         try:
#             data = fetch_url_data(url, get_core)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         new_assessment = CoreAssessments.objects.create(trainee=request.user)
#         for i in range(len(data[0])):
#             test = CoreTest(
#                 assessment=new_assessment,
#                 first_trial=data[0][i],
#                 second_trial=data[1][i],
#             )

#             test.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def update_core_test(request, test_id):
#     if request.method == "PUT":
#         url = request.data.get("url")
#         if not url:
#             return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             data = fetch_url_data(url, get_core)
#         except requests.RequestException as e:
#             return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         test_queryset = CoreTest.objects.filter(id=test_id)
#         if not test_queryset.exists():
#             return Response(
#                 {"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         test_instance = test_queryset.first()

#         for i in range(len(data[0])):
#             try:
#                 test_instance.first_trial = data[0][i]
#                 test_instance.second_trial = data[1][i]
#                 test_instance.save()
#             except (
#                 InvalidOperation,
#                 ValidationError,
#             ) as e:  # ValidationError in case there's any issue during saving.
#                 return Response(
#                     {"error": f"Invalid data: {str(e)}"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )

#     return Response(
#         {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
#     )


# def delete_core_test(request, test_id):
#     test = CoreTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )


# #!Shark Skills Test
# def get_shark_skills_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     assessments = SharkSkillsAssessments.objects.filter(trainee=user)
#     serializer = SharkSkillsAssessmentsSerializer(assessments, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# def delete_shark_skills_assessments(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user and not request.user.is_superuser:
#         return Response(
#             {"message": "You do not have permission to delete this user's assessments"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
#     assessments = SharkSkillsAssessments.objects.filter(trainee=user)
#     assessments.delete()

#     return Response(
#         {"message": "Assessments have been deleted successfully"},
#         status=status.HTTP_200_OK,
#     )


# def input_shark_skills_test(request):
#     url = request.data.get("url")
#     if not url:
#         return Response(
#                 {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#             )
#     try:
#         fetched_data = fetch_url_data(url, get_sharks_skills)

#     except requests.RequestException as e:
#         return Response(
#                 {"error": f"Failed to fetch data from {url}: {str(e)}"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#     new_assessment = SharkSkillsAssessments.objects.create(trainee=request.user)

#     for test_set_data in fetched_data:
#         test_instance = SharkSkillsTest(assessment=new_assessment)

#             # For each side, create an instance of SharkSkillsSide and associate it with the test_instance
#         for side_key, side_data in test_set_data.items():
#             side_instance = SharkSkillsSide.objects.create(
#                 time=side_data["time"],
#                 deduction_tally=side_data["deduction_tally"],
#                 total_deducted=side_data["total_deducted"],
#                 final_total=side_data["final_total"],
#                 )
#                 # Determine which attribute of test_instance to associate the side_instance with
#             side_attr = side_key.split("_")[-2] + "_" + side_key.split("_")[-1]
#             setattr(test_instance, side_attr, side_instance)

#         test_instance.save()

#     return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )



# def get_shark_skills_test(request, test_id):
#     # TODO make consistent with .object or getobjector404 lean swap to .object and filter
#     test = get_object_or_404(SharkSkillsTest, id=test_id)
#     serializer = SharkSkillsTestSerializer(test)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# # TODO fix with formatting of data for input via sheets
# def update_shark_skills_test(request, test_id):
#     url = request.data.get("url")
#     if not url:
#         return Response(
#             {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
#         )

#     try:
#         fetched_data = fetch_url_data(url, get_sharks_skills)
#     except requests.RequestException as e:
#         return Response(
#             {"error": f"Failed to fetch data from {url}: {str(e)}"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     test_queryset = SharkSkillsTest.objects.filter(id=test_id)
#     if not test_queryset.exists():
#         return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)
#     test_instance = test_queryset.first()

#     for test_set_data in fetched_data:
#         for side_key, side_data in test_set_data.items():
#             side_attr = side_key.split("_")[-2] + "_" + side_key.split("_")[-1]
#             side_instance = getattr(test_instance, side_attr)

#             side_instance.time = side_data["time"]
#             side_instance.deduction_tally = side_data["deduction_tally"]
#             side_instance.total_deducted = side_data["total_deducted"]
#             side_instance.final_total = side_data["final_total"]
#             side_instance.save()

#         test_instance.save()

#     return Response(
#             {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
#         )



# def delete_shark_skills_test(request, test_id):
#     test = SharkSkillsTest.objects.filter(id=test_id)
#     test.delete()

#     return Response(
#         {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
#     )
