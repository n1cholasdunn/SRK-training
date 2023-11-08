from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from common.models.climbing_models import MaxPullupsTest
from common.utils.climbing_serializers import MaxPullupsTestSerializer
from rest_framework.request import Request
from typing import List, Dict


def get_max_pullups_tests(request: Request) -> Response:
    tests = MaxPullupsTest.objects.all()
    serializer = MaxPullupsTestSerializer(tests, many=True)
    return Response({"max_pullups": {"tests": serializer.data}})


def get_max_pullups_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(MaxPullupsTest, pk=pk)
    serializer = MaxPullupsTestSerializer(test)
    return Response({"max_pullups": {f"test  {pk}": serializer.data}})


def create_max_pullups_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("max_pullups", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    created_tests = []
    for test_data in data:
        serializer = MaxPullupsTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"max_pullups": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_max_pullups_test(request: Request, pk: int) -> Response:
    try:
        test_instance = MaxPullupsTest.objects.get(pk=pk)
    except MaxPullupsTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaxPullupsTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_max_pullups_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(MaxPullupsTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
