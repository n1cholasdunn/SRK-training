from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from common.models.climbing_models import PowerEnduranceAssessments
from common.utils.climbing_serializers import PowerEnduranceAssessmentsSerializer


def get_power_endurance_assessment(request):
    user = request.user
    assessment = get_object_or_404(PowerEnduranceAssessments, trainee=user)
    serializer = PowerEnduranceAssessmentsSerializer(assessment)
    return Response(serializer.data)


def create_power_endurance_assessment(request):
    data = request.data.get("power_endurance")
    serializer = PowerEnduranceAssessmentsSerializer(
        data=data, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save(trainee=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_power_endurance_assessment(request, pk):
    try:
        assessment = PowerEnduranceAssessments.objects.get(pk=pk, trainee=request.user)
    except PowerEnduranceAssessments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PowerEnduranceAssessmentsSerializer(
        assessment, data=request.data, partial=request.method == "PATCH"
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_power_endurance_assessment(request, pk):
    try:
        assessment = PowerEnduranceAssessments.objects.get(pk=pk, trainee=request.user)
    except PowerEnduranceAssessments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    assessment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
