from core.models import User
from django.shortcuts import get_object_or_404
from planApi.gsheets.getters.get_client import get_availability
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from planApi.models.client_models import ClientAvailability
from planApi.models.common import BaseClientInfo
import requests
from rest_framework import status
from rest_framework.response import Response


def retrieve_client_availability(request, user_id):
    availability = get_object_or_404(ClientAvailability, id=user_id)
    return Response(
        {
            "monday": availability.monday_id,
            "tuesday": availability.tuesday_id,
            "wednesday": availability.wednesday_id,
            "thursday": availability.thursday_id,
            "friday": availability.friday_id,
            "saturday": availability.saturday_id,
            "sunday": availability.sunday_id,
        }
    )


def create_client_availability(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_availability)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        availability = ClientAvailability.objects.create(
            monday_id=data.get("monday"),
            tuesday_id=data.get("tuesday"),
            wednesday_id=data.get("wednesday"),
            thursday_id=data.get("thursday"),
            friday_id=data.get("friday"),
            saturday_id=data.get("saturday"),
            sunday_id=data.get("sunday"),
            trainee=request.user,
        )
        availability.save()

        return Response(
            {"message": "Client availability created successfully!"},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def delete_client_availability(request, user_id):
    if request.method == "DELETE":
        availability = get_object_or_404(ClientAvailability, id=user_id)
        availability.delete()
        return Response(
            {"message": "Client availability deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )
