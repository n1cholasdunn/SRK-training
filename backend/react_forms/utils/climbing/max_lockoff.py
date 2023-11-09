from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.climbing_models import MaxLockoffTest
from common.utils.climbing_serializers import MaxLockoffTestSerializer
from typing import List, Dict


def get_max_lockoff_tests(request: Request) -> Response:
    tests = MaxLockoffTest.objects.all()
    serializer = MaxLockoffTestSerializer(tests, many=True)
    return Response({"max_lockoff": {"tests": serializer.data}})


def get_max_lockoff_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(MaxLockoffTest, pk=pk)
    serializer = MaxLockoffTestSerializer(test)
    return Response({"max_lockoff": {f"test  {pk}": serializer.data}})


def create_max_lockoff_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("max_lockoff", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = MaxLockoffTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"max_lockoff": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_max_lockoff_test(request: Request, pk: int) -> Response:
    try:
        test_instance = MaxLockoffTest.objects.get(pk=pk)
    except MaxLockoffTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaxLockoffTestSerializer(
        test_instance, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_max_lockoff_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(MaxLockoffTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
