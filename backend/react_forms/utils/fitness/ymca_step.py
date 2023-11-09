from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.fitness_models import YMCAStepTest
from common.utils.fitness_serializers import YMCAStepTestSerializer
from typing import List, Dict


def get_ymca_step_tests(request: Request) -> Response:
    tests = YMCAStepTest.objects.all()
    serializer = YMCAStepTestSerializer(tests, many=True)
    return Response({"ymca_step": {"tests": serializer.data}})


def get_ymca_step_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(YMCAStepTest, pk=pk)
    serializer = YMCAStepTestSerializer(test)
    return Response({"ymca_step": {f"test  {pk}": serializer.data}})


def create_ymca_step_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("ymca_step", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = YMCAStepTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"ymca_step": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_ymca_step_test(request: Request, pk: int) -> Response:
    try:
        test_instance = YMCAStepTest.objects.get(pk=pk)
    except YMCAStepTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = YMCAStepTestSerializer(test_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_ymca_step_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(YMCAStepTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
