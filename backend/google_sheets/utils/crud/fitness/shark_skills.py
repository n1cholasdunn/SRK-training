from core.models import User
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response
from google_sheets.utils.getters.get_fitness_assessments import get_sharks_skills
from common.models.fitness_models import (
    SharkSkillsAssessments,
    SharkSkillsSide,
    SharkSkillsTest,
)
from common.utils.fitness_serializers import (
    SharkSkillsAssessmentsSerializer,
    SharkSkillsTestSerializer,
)


def get_shark_skills_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    assessments = SharkSkillsAssessments.objects.filter(trainee=user)
    serializer = SharkSkillsAssessmentsSerializer(assessments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_shark_skills_assessments(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user and not request.user.is_superuser:
        return Response(
            {"message": "You do not have permission to delete this user's assessments"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    assessments = SharkSkillsAssessments.objects.filter(trainee=user)
    assessments.delete()

    return Response(
        {"message": "Assessments have been deleted successfully"},
        status=status.HTTP_200_OK,
    )


def input_shark_skills_test(request):
    url = request.data.get("url")
    if not url:
        return Response(
            {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        fetched_data = fetch_url_data(url, get_sharks_skills)

    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    new_assessment = SharkSkillsAssessments.objects.create(trainee=request.user)

    for test_set_data in fetched_data:
        test_instance = SharkSkillsTest(assessment=new_assessment)

        # For each side, create an instance of SharkSkillsSide and associate it with the test_instance
        for side_key, side_data in test_set_data.items():
            side_instance = SharkSkillsSide.objects.create(
                time=side_data["time"],
                deduction_tally=side_data["deduction_tally"],
                total_deducted=side_data["total_deducted"],
                final_total=side_data["final_total"],
            )
            # Determine which attribute of test_instance to associate the side_instance with
            side_attr = side_key.split("_")[-2] + "_" + side_key.split("_")[-1]
            setattr(test_instance, side_attr, side_instance)

        test_instance.save()

    return Response(
        {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
    )


def get_shark_skills_test(request, test_id):
    # TODO make consistent with .object or getobjector404 lean swap to .object and filter
    test = get_object_or_404(SharkSkillsTest, id=test_id)
    serializer = SharkSkillsTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO fix with formatting of data for input via sheets
def update_shark_skills_test(request, test_id):
    url = request.data.get("url")
    if not url:
        return Response(
            {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        fetched_data = fetch_url_data(url, get_sharks_skills)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    test_queryset = SharkSkillsTest.objects.filter(id=test_id)
    if not test_queryset.exists():
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)
    test_instance = test_queryset.first()

    for test_set_data in fetched_data:
        for side_key, side_data in test_set_data.items():
            side_attr = side_key.split("_")[-2] + "_" + side_key.split("_")[-1]
            side_instance = getattr(test_instance, side_attr)

            side_instance.time = side_data["time"]
            side_instance.deduction_tally = side_data["deduction_tally"]
            side_instance.total_deducted = side_data["total_deducted"]
            side_instance.final_total = side_data["final_total"]
            side_instance.save()

        test_instance.save()

    return Response(
        {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
    )


def delete_shark_skills_test(request, test_id):
    test = SharkSkillsTest.objects.filter(id=test_id)
    test.delete()

    return Response(
        {"message": "Test has been deleted successfully"}, status=status.HTTP_200_OK
    )
