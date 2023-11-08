from common.utils.client_serializers import DayAvailabilitySerializer
from django.shortcuts import get_object_or_404
from common.models.client_models import (
    DayAvailability,
    GeneralClientInfo,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request


def get_availabilities(request: Request) -> Response:
    user = request.user
    general_client_info = get_object_or_404(GeneralClientInfo, trainee=user)
    availabilities = DayAvailability.objects.filter(client=general_client_info)
    serializer = DayAvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data)


def get_availability_by_id(request: Request, pk: int) -> Response:
    general_client_info = get_object_or_404(GeneralClientInfo, trainee=pk)
    availabilities = DayAvailability.objects.filter(client=general_client_info)
    serializer = DayAvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data)


def create_availability(request: Request) -> Response:
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


def update_availability(request: Request) -> Response:
    user = request.user
    try:
        availability = DayAvailability.objects.get(client__trainee=user)
    except DayAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DayAvailabilitySerializer(availability, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_availability(request: Request) -> Response:
    user = request.user
    try:
        availability = DayAvailability.objects.get(client__trainee=user)
    except DayAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    availability.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
