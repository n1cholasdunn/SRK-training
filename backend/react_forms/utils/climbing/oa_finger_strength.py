from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.climbing_models import OAFingerStrengthTest
from common.utils.climbing_serializers import OAFingerStrengthTestSerializer
from typing import List, Dict


def get_oa_finger_strength_tests(request: Request) -> Response:
    tests: List[OAFingerStrengthTest] = OAFingerStrengthTest.objects.all()
    serializer = OAFingerStrengthTestSerializer(tests, many=True)
    return Response({"oa_finger_strength": {"tests": serializer.data}})


def get_oa_finger_strength_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(OAFingerStrengthTest, pk=pk)
    serializer = OAFingerStrengthTestSerializer(test)
    return Response({"oa_finger_strength": {f"test  {pk}": serializer.data}})


def create_oa_finger_strength_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("oa_finger_strength", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    created_tests = []
    for test_data in data:
        serializer = OAFingerStrengthTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"oa_finger_strength": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_oa_finger_strength_test(request: Request, pk: int) -> Response:
    try:
        test_instance = OAFingerStrengthTest.objects.get(pk=pk)
    except OAFingerStrengthTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OAFingerStrengthTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_oa_finger_strength_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(OAFingerStrengthTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
