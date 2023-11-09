from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.fitness_models import CoreTest
from common.utils.fitness_serializers import CoreTestSerializer
from typing import List, Dict


def get_core_tests(request: Request) -> Response:
    tests = CoreTest.objects.all()
    serializer = CoreTestSerializer(tests, many=True)
    return Response({"core": {"tests": serializer.data}})


def get_core_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(CoreTest, pk=pk)
    serializer = CoreTestSerializer(test)
    return Response({"core": {f"test  {pk}": serializer.data}})


def create_core_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("core", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = CoreTestSerializer(data=test_data, context={"request": request})
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"core": {"tests": created_tests}}, status=status.HTTP_201_CREATED)


def update_core_test(request: Request, pk: int) -> Response:
    try:
        test_instance = CoreTest.objects.get(pk=pk)
    except CoreTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CoreTestSerializer(test_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_core_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(CoreTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
