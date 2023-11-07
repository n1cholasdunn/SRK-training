from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from react_forms.utils.client.general_client_info import (
    create_general_client_info,
    delete_general_client_info,
    get_general_client_info,
    update_general_client_info,
)

from react_forms.utils.client.availability import (
    create_availability,
    delete_availability,
    get_availabilities,
    update_availability,
)


@api_view(["GET", "PUT", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_availability(request, pk):
    if request.method == "GET":
        return get_availabilities(request)
    if request.method == "PUT":
        return update_availability(request, pk)
    if request.method == "POST":
        return create_availability(request)
    if request.method == "DELETE":
        return delete_availability(request, pk)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_general_client_info_input(request):
    if request.method == "POST":
        return create_general_client_info(request)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_general_client_info(request, pk):
    if request.method == "GET":
        return get_general_client_info(request)
    if request.method == "PUT":
        return update_general_client_info(request, pk)
    if request.method == "POST":
        return create_general_client_info(request)
    if request.method == "DELETE":
        return delete_general_client_info(request, pk)
