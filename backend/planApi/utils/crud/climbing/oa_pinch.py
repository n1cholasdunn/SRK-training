from backend.planApi.gsheets.getters.get_climbing_assessments import (
    get_oa_pinch_finger_strength,
)
from core.models import User
from django.forms import ValidationError
import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.models.climbing_models import OAPinchAssessments, OAPinchTest
from planApi.utils.serializers.climbing import (
    OAPinchAssessmentsSerializer,
    OAPinchTestSerializer,
)


def get_oa_pinch_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = OAPinchAssessments.objects.filter(trainee=user)
    serializer = OAPinchAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_oa_pinch_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = OAPinchAssessments.objects.filter(trainee=user)
    assessments.delete()
    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_oa_pinch_test(request, test_id):
    test = get_object_or_404(OAPinchTest, id=test_id)
    serializer = OAPinchTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_oa_pinch_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_oa_pinch_finger_strength)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_assessment = OAPinchAssessments.objects.create(trainee=request.user)

        for test_data in data:
            test = OAPinchTest(
                assessment=new_assessment,
                test=test_data["Test"],
                left=test_data["Left"],
                right=test_data["Right"],
            )
            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_oa_pinch_test(request):
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
        data = fetch_url_data(url, get_oa_pinch_finger_strength)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        test_instance = OAPinchTest.objects.get(id=test_id)
    except OAPinchTest.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

    for item in data:
        # TODO change all accessing to be dot notation isntead of bracket as well
        test_instance.left = item.Left
        test_instance.right = item.Right
        test_instance.save()

        return Response(
            {"message": f"Test with ID {test_id} updated successfully!"},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "No matching data found for the test in the fetched data"},
        status=status.HTTP_400_BAD_REQUEST,
    )


def delete_oa_pinch_test(request, test_id):
    test = OAPinchTest.objects.filter(id=test_id)
    test.delete()
    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
