from core.models import User
from django.forms import ValidationError
from planApi.gsheets.getters.get_climbing_assessments import get_oa_finger_strength
import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.models.climbing_models import (
    OAFingerStrengthAssessments,
    OAFingerStrengthTest,
)
from planApi.utils.serializers.climbing import (
    OAFingerStrengthAssessmentsSerializer,
    OAFingerStrengthTestSerializer,
)


def get_oa_finger_strength_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = OAFingerStrengthAssessments.objects.filter(trainee=user)
    serializer = OAFingerStrengthAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_oa_finger_strength_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = OAFingerStrengthAssessments.objects.filter(trainee=user)
    assessments.delete()
    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_oa_finger_strength_test(request, test_id):
    test = get_object_or_404(OAFingerStrengthTest, id=test_id)
    serializer = OAFingerStrengthTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_oa_finger_strength_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_oa_finger_strength)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_assessment = OAFingerStrengthAssessments.objects.create(
            trainee=request.user
        )

        for test_data in data:
            test = OAFingerStrengthTest(
                assessment=new_assessment,
                test=test_data["Test"],
                left=test_data["Left"],
                right=test_data["Right"],
                left_percentage=test_data["LeftPercentage"],
                right_percentage=test_data["RightPercentage"],
            )
            test.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_oa_finger_strength_test_from_url(request):
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
        data = fetch_url_data(url, get_oa_finger_strength)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        existing_test = OAFingerStrengthTest.objects.get(id=test_id)
    except OAFingerStrengthTest.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

    for item in data:
        existing_test.left = item["Left"]
        existing_test.right = item["Right"]
        existing_test.left_percentage = item["LeftPercentage"]
        existing_test.right_percentage = item["RightPercentage"]
        existing_test.save()

        return Response(
            {"message": f"Test with ID {test_id} updated successfully!"},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "No matching data found for the test in the fetched data"},
        status=status.HTTP_400_BAD_REQUEST,
    )


def delete_oa_finger_strength_test(request, test_id):
    test = OAFingerStrengthTest.objects.filter(id=test_id)
    test.delete()
    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
