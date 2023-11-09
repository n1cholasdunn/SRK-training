from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.climbing_models import OAPinchTest
from common.utils.climbing_serializers import OAPinchTestSerializer
from typing import List, Dict


def get_oa_pinch_strength_tests(request: Request) -> Response:
    tests: List[OAPinchTest] = OAPinchTest.objects.all()
    serializer = OAPinchTestSerializer(tests, many=True)
    return Response({"oa_pinch_strength": {"tests": serializer.data}})


def get_oa_pinch_strength_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(OAPinchTest, pk=pk)
    serializer = OAPinchTestSerializer(test)
    return Response({"oa_pinch_strength": {f"test  {pk}": serializer.data}})


def create_oa_pinch_strength_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("oa_pinch_strength", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    created_tests = []
    for test_data in data:
        serializer = OAPinchTestSerializer(data=test_data, context={"request": request})
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"oa_pinch_strength": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_oa_pinch_strength_test(request: Request, pk: int) -> Response:
    try:
        test_instance = OAPinchTest.objects.get(pk=pk)
    except OAPinchTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OAPinchTestSerializer(test_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_oa_pinch_strength_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(OAPinchTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
