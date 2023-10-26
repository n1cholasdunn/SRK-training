from core.models import User
from django.forms import ValidationError
from planApi.gsheets.getters.get_climbing_assessments import get_max_pullups
import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.models.climbing_models import MaxPullupsAssessments, MaxPullupsTest
from planApi.utils.serializers.climbing import (
    MaxPullupsAssessmentsSerializer,
    MaxPullupsTestSerializer,
)


def get_max_pullups_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = MaxPullupsAssessments.objects.filter(trainee=user)
    serializer = MaxPullupsAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_max_pullups_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = MaxPullupsAssessments.objects.filter(trainee=user)
    assessments.delete()
    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_max_pullups_test(request, test_id):
    test = get_object_or_404(MaxPullupsTest, id=test_id)
    serializer = MaxPullupsTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_max_pullups_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_max_pullups)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_assessment = MaxPullupsAssessments.objects.create(trainee=request.user)

        test_names = data[0]
        values = data[1]

        for i in range(len(test_names)):
            test = MaxPullupsTest(
                assessment=new_assessment,
                test=test_names[i],
                reps=values[i],
            )
            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_max_pullups_test(request):
    test_id = request.data.get("id")
    url = request.data.get("url")
    if not test_id:
        return Response(
            {"error": "Test ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not url:
        return Response(
            {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        data = fetch_url_data(url, get_max_pullups)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        test_instance = MaxPullupsTest.objects.get(id=test_id)
    except MaxPullupsTest.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

    test_names = data[0]
    values = data[1]

    for i in range(len(test_names)):
        try:
            test_instance.test = test_names[i]
            test_instance.reps = values[i]
        except ValidationError as e:
            return Response(
                {"error": f"Invalid data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    test_instance.save()

    return Response(
        {"error": "No matching data found for the test in the fetched data"},
        status=status.HTTP_400_BAD_REQUEST,
    )


def delete_max_pullups_test(request, test_id):
    test = MaxPullupsTest.objects.filter(id=test_id)
    test.delete()
    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
