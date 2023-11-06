from core.models import User
from django.forms import ValidationError
from planApi.models.client_models import ClientProgramInfo
import requests
from rest_framework import status
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
from rest_framework.response import Response


def retrieve_client_program_info(request, program_info_id):
    program_info = get_object_or_404(ClientProgramInfo, id=program_info_id)
    return Response(
        {
            "program_type": program_info.program_type,
            "training_style": program_info.training_style,
            "payment_rate": program_info.payment_rate,
            "program_start": program_info.program_start,
            "outdoor_max": program_info.outdoor_max,
            "outdoor_flash": program_info.outdoor_flash,
            "indoor_max": program_info.indoor_max,
            "indoor_flash": program_info.indoor_flash,
        }
    )


def create_client_program_info(request):
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
            program_info = ClientProgramInfo.objects.create(
                program_type=data.get("program_type"),
                training_style=data.get("training_style"),
                payment_rate=data.get("payment_rate"),
                program_start=data.get("program_start"),
                outdoor_max=data.get("outdoor_max"),
                outdoor_flash=data.get("outdoor_flash"),
                indoor_max=data.get("indoor_max"),
                indoor_flash=data.get("indoor_flash"),
            )
            program_info.save()
        except ValidationError as e:
            return Response(
                {"error": f"Invalid data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Client program info created successfully!"},
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_client_program_info(request, program_info_id):
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

        program_info = get_object_or_404(ClientProgramInfo, id=program_info_id)
        for key, value in data.items():
            setattr(program_info, key, value)

        try:
            program_info.save()
        except ValidationError as e:
            return Response(
                {"error": f"Invalid data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Client program info updated successfully!"},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def delete_client_program_info(request, program_info_id):
    if request.method == "DELETE":
        program_info = get_object_or_404(ClientProgramInfo, id=program_info_id)
        program_info.delete()
        return Response(
            {"message": "Client program info deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )
