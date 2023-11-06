from core.models import User
from django.forms import ValidationError
from planApi.models.client_models import ClientEquipment
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response


def retrieve_client_equipment(request, equipment_id):
    equipment = get_object_or_404(ClientEquipment, id=equipment_id)
    return Response({"equipment": equipment.equipment_id})


def create_client_equipment(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            equipment = ClientEquipment.objects.create(
                equipment_id=data.get("equipment")
            )
            equipment.save()
        except ValidationError as e:
            return Response(
                {"error": f"Invalid data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Client equipment created successfully!"},
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_client_equipment(request, equipment_id):
    if request.method == "PUT":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        equipment_queryset = ClientEquipment.objects.filter(id=equipment_id)
        if not equipment_queryset.exists():
            return Response(
                {"error": "Client Equipment not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        equipment_instance = equipment_queryset.first()

        try:
            # TODO test to see if this works
            equipment_instance.equipment_id = data.get(
                "equipment", equipment_instance.equipment_id
            )

            equipment_instance.save()

        except ValidationError as e:
            return Response(
                {"error": f"Invalid data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Client equipment updated successfully!"},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def delete_client_equipment(request, equipment_id):
    if request.method == "DELETE":
        equipment = get_object_or_404(ClientEquipment, id=equipment_id)
        equipment.delete()
        return Response(
            {"message": "Client equipment deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )
