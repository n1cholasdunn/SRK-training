from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.fitness_models import HealthMarkersTest
from common.utils.fitness_serializers import HealthMarkersTestSerializer
from typing import List, Dict


def get_health_markers_tests(request: Request) -> Response:
    tests = HealthMarkersTest.objects.all()
    serializer = HealthMarkersTestSerializer(tests, many=True)
    return Response({"health_markers": {"tests": serializer.data}})


def get_health_markers_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(HealthMarkersTest, pk=pk)
    serializer = HealthMarkersTestSerializer(test)
    return Response({"health_markers": {f"test  {pk}": serializer.data}})


def create_health_markers_test(request: Request) -> Response:
    data: List[Dict[str, int | str]] = request.data.get("health_markers", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = HealthMarkersTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"health_markers": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_health_markers_test(request: Request, pk: int) -> Response:
    try:
        test_instance = HealthMarkersTest.objects.get(pk=pk)
    except HealthMarkersTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = HealthMarkersTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_health_markers_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(HealthMarkersTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
