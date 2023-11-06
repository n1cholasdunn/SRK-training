from planApi.utils.serializers.client import DayAvailabilitySerializer
from django.shortcuts import get_object_or_404
from planApi.models.client_models import (
    DayAvailability,
    GeneralClientInfo,
)
from rest_framework import status
from rest_framework.response import Response


def get_availabilities(request):
    user = request.user
    general_client_info = get_object_or_404(GeneralClientInfo, trainee=user)
    availabilities = DayAvailability.objects.filter(client=general_client_info)
    serializer = DayAvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data)


def create_availability(request):
    user = request.user
    general_client_info = get_object_or_404(GeneralClientInfo, trainee=user)
    request.data[
        "client"
    ] = general_client_info.pk  # Set the client in the request data
    serializer = DayAvailabilitySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_availability(request, pk):
    user = request.user
    try:
        availability = DayAvailability.objects.get(pk=pk, client__trainee=user)
    except DayAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DayAvailabilitySerializer(availability, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_availability(request, pk):
    user = request.user
    try:
        availability = DayAvailability.objects.get(pk=pk, client__trainee=user)
    except DayAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    availability.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
