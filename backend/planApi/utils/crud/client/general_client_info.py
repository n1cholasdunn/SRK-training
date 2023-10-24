from core.models import User
from django.shortcuts import get_object_or_404
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
import requests
from rest_framework import status
from rest_framework.response import Response
from planApi.models.client_models import GeneralClientInfo
from planApi.utils.serializers.client import (
    GeneralClientInfoSerializer,
)


def get_general_client_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    client_info = get_object_or_404(GeneralClientInfo, user=user)
    serializer = GeneralClientInfoSerializer(client_info)
    return Response(serializer.data, status=status.HTTP_200_OK)


def create_general_client_info(request):
    if request.method == "POST":
        serializer = GeneralClientInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_general_client_info(request, user_id):
    client_info = get_object_or_404(GeneralClientInfo, user_id=user_id)
    serializer = GeneralClientInfoSerializer(instance=client_info, data=request.data)
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
