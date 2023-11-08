from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from common.models.climbing_models import FingerStrengthTest
from common.utils.climbing_serializers import FingerStrengthTestSerializer
from typing import List, Dict


def get_finger_strength_tests(request: Request) -> Response:
    tests = FingerStrengthTest.objects.all()
    serializer = FingerStrengthTestSerializer(tests, many=True)
    return Response({"finger_strength": {"tests": serializer.data}})


def get_finger_strength_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(FingerStrengthTest, pk=pk)
    serializer = FingerStrengthTestSerializer(test)
    return Response({"finger_strength": {f"test  {pk}": serializer.data}})


def create_finger_strength_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("finger_strength", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    created_tests = []
    for test_data in data:
        serializer = FingerStrengthTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"finger_strength": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_finger_strength_test(request: Request, pk: int) -> Response:
    try:
        test_instance = FingerStrengthTest.objects.get(pk=pk)
    except FingerStrengthTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = FingerStrengthTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_finger_strength_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(FingerStrengthTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
