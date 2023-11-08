from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from typing import List, Dict
from common.models.climbing_models import PowerEnduranceTest
from common.utils.climbing_serializers import PowerEnduranceTestSerializer


def get_power_endurance_tests(request: Request) -> Response:
    tests = PowerEnduranceTest.objects.all()
    serializer = PowerEnduranceTestSerializer(tests, many=True)
    return Response({"power_endurance": {"tests": serializer.data}})


def get_power_endurance_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(PowerEnduranceTest, pk=pk)
    serializer = PowerEnduranceTestSerializer(test)
    return Response({"power_endurance": {f"test  {pk}": serializer.data}})


def create_power_endurance_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("power_endurance", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    created_tests = []
    for test_data in data:
        serializer = PowerEnduranceTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"power_endurance": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_power_endurance_test(request: Request, pk: int) -> Response:
    try:
        test_instance = PowerEnduranceTest.objects.get(pk=pk)
    except PowerEnduranceTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PowerEnduranceTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_power_endurance_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(PowerEnduranceTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
