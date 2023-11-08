from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from common.models.climbing_models import PowerEnduranceTest
from common.utils.climbing_serializers import PowerEnduranceTestSerializer


def get_power_endurance_tests(request):
    tests = PowerEnduranceTest.objects.all()
    serializer = PowerEnduranceTestSerializer(tests, many=True)
    return Response(serializer.data)


def create_power_endurance_test(request):
    data = request.data.get("power_endurance", {}).get("tests")
    if data:
        # This assumes that the request includes the assessment id under which to file these tests
        assessment_id = request.data.get(
            "assessment_id"
        )  # You'll need to pass this in the request
        assessment = get_object_or_404(ClimbingAssessments, pk=assessment_id)

        created_tests = []
        for test_data in data:
            serializer = PowerEnduranceTestSerializer(data=test_data)
            if serializer.is_valid():
                test = serializer.save(assessment=assessment)
                created_tests.append(test)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        created_data = PowerEnduranceTestSerializer(created_tests, many=True).data
        return Response(created_data, status=status.HTTP_201_CREATED)
    return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


def update_power_endurance_test(request, pk):
    test = get_object_or_404(PowerEnduranceTest, pk=pk)
    serializer = PowerEnduranceTestSerializer(test, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_power_endurance_test(request, pk):
    test = get_object_or_404(PowerEnduranceTest, pk=pk)
    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
