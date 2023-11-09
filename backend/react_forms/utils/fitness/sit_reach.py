from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.fitness_models import SitReachTest
from common.utils.fitness_serializers import SitReachTestSerializer
from typing import List, Dict


def get_sit_reach_tests(request: Request) -> Response:
    tests = SitReachTest.objects.all()
    serializer = SitReachTestSerializer(tests, many=True)
    return Response({"sit_reach": {"tests": serializer.data}})


def get_sit_reach_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(SitReachTest, pk=pk)
    serializer = SitReachTestSerializer(test)
    return Response({"sit_reach": {f"test  {pk}": serializer.data}})


def create_sit_reach_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("sit_reach", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = SitReachTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"sit_reach": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_sit_reach_test(request: Request, pk: int) -> Response:
    try:
        test_instance = SitReachTest.objects.get(pk=pk)
    except SitReachTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = SitReachTestSerializer(test_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_sit_reach_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(SitReachTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
