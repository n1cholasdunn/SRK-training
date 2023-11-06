from google_sheets.utils.getters.get_client import get_client_info
from core.models import User
from django.shortcuts import get_object_or_404
from google_sheets.utils.fetch_by_url import fetch_url_data
import requests
from rest_framework import status
from rest_framework.response import Response
from common.models.client_models import GeneralClientInfo
from common.utils.client_serializers import (
    GeneralClientInfoSerializer,
)


def get_general_client_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    client_info = get_object_or_404(GeneralClientInfo, user=user)
    serializer = GeneralClientInfoSerializer(client_info)
    return Response(serializer.data, status=status.HTTP_200_OK)


def create_general_client_info(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = fetch_url_data(url, get_client_info)
        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GeneralClientInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_general_client_info(request, user_id):
    url = request.data.get("url")
    if not url:
        return Response(
            {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        data = fetch_url_data(url, get_client_info)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch data from {url}: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    client_info = get_object_or_404(GeneralClientInfo, user_id=user_id)
    serializer = GeneralClientInfoSerializer(instance=client_info, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_general_client_info(request, user_id):
    client_info = get_object_or_404(GeneralClientInfo, user_id=user_id)
    client_info.delete()
    return Response(
        {"message": "Client information deleted successfully"},
        status=status.HTTP_200_OK,
    )
