from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from common.models.fitness_models import SharkSkillsTest
from common.utils.fitness_serializers import SharkSkillsTestSerializer
from typing import List, Dict


def get_shark_skills_tests(request: Request) -> Response:
    if request.method == "GET":
        shark_skills_tests = SharkSkillsTest.objects.filter(trainee=request.user)
        serializer = SharkSkillsTestSerializer(shark_skills_tests, many=True)
        return Response(serializer.data)


def get_shark_skills_test_by_id(request: Request, pk: int) -> Response:
    try:
        shark_skills_test = SharkSkillsTest.objects.get(pk=pk)
    except SharkSkillsTest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SharkSkillsTestSerializer(shark_skills_test)
    return Response(serializer.data)


def create_shark_skills_test(request: Request) -> Response:
    data: List[Dict[str, Dict[str, int]]] = request.data.get("shark_skills", {}).get(
        "tests", []
    )

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = SharkSkillsTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save(trainee=request.user)
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"shark_skills": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def create_shark_skills_test(request: Request) -> Response:
    data: List[Dict[str, int]] = request.data.get("shark_skills", {}).get("tests", [])

    if not isinstance(data, list):
        return Response(
            {"error": "Invalid data format, expected a list of tests."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    created_tests = []
    for test_data in data:
        serializer = SharkSkillsTestSerializer(
            data=test_data, context={"request": request}
        )
        if serializer.is_valid():
            test_instance = serializer.save()
            created_tests.append(serializer.data)
            print(created_tests)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"shark_skills": {"tests": created_tests}}, status=status.HTTP_201_CREATED
    )


def update_shark_skills_test(request: Request, pk: int) -> Response:
    try:
        shark_skills_test = SharkSkillsTest.objects.get(pk=pk)
    except SharkSkillsTest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SharkSkillsTestSerializer(shark_skills_test, data=request.data)
    if serializer.is_valid():
        serializer.save(trainee=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_shark_skills_test(request: Request, pk: int) -> Response:
    try:
        shark_skills_test = SharkSkillsTest.objects.get(pk=pk)
    except SharkSkillsTest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    shark_skills_test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
