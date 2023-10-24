from core.models import User
from django.forms import ValidationError
import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.models.climbing_models import FingerStrengthAssessments, FingerStrengthTest
from planApi.utils.serializers.climbing import (
    FingerStrengthAssessmentsSerializer,
    FingerStrengthTestSerializer,
)


def get_finger_strength_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = FingerStrengthAssessments.objects.filter(trainee=user)
    serializer = FingerStrengthAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_finger_strength_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = FingerStrengthAssessments.objects.filter(trainee=user)
    assessments.delete()
    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def get_finger_strength_test(request, test_id):
    test = get_object_or_404(FingerStrengthTest, id=test_id)
    serializer = FingerStrengthTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_finger_strength_test(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_finger_strength_test)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_assessment = FingerStrengthAssessments.objects.create(trainee=request.user)
        for i in range(len(data[0])):
            test = FingerStrengthTest(
                assessment=new_assessment,
                test=float(data[0][i]),
                # TODO structure data
            )
            test.save()
        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_finger_strength_test(request, test_id):
    try:
        test_instance = FingerStrengthTest.objects.get(id=test_id)
    except FingerStrengthTest.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FingerStrengthTestSerializer(instance=test_instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_finger_strength_test(request, test_id):
    test = FingerStrengthTest.objects.filter(id=test_id)
    test.delete()
    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
