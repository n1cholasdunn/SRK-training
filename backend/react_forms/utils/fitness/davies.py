from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from common.models.fitness_models import DaviesTest
from common.utils.fitness_serializers import DaviesTestSerializer
from typing import List, Dict


def get_davies_tests(request: Request) -> Response:
    tests = DaviesTest.objects.all()
    serializer = DaviesTestSerializer(tests, many=True)
    return Response({"davies": {"tests": serializer.data}})


def get_davies_test_by_id(request: Request, pk: int) -> Response:
    test = get_object_or_404(DaviesTest, pk=pk)
    serializer = DaviesTestSerializer(test)
    return Response({"davies": {f"test  {pk}": serializer.data}})


def create_davies_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("davies", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = DaviesTestSerializer(data=test_data, context={"request": request})
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"davies": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_davies_test(request: Request, pk: int) -> Response:
    try:
        test_instance = DaviesTest.objects.get(pk=pk)
    except DaviesTest.DoesNotExist:
        return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = DaviesTestSerializer(test_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_davies_test(request: Request, pk: int) -> Response:
    test = get_object_or_404(DaviesTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
