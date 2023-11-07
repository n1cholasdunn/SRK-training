from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from react_forms.utils.client.equipment import (
    create_equipment,
    delete_equipment,
    get_equipment,
    update_equipment,
)
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

from react_forms.utils.client.program import (
    get_program,
    create_program,
    update_program,
    delete_program,
)

from react_forms.utils.climbing.power_endurance import (
    get_power_endurance_assessment,
    create_power_endurance_assessment,
    update_power_endurance_assessment,
    delete_power_endurance_assessment,
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


@api_view(["GET", "PUT", "POST", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_general_client_info(request):
    if request.method == "GET":
        return get_general_client_info(request)
    if request.method == "PUT":
        return update_general_client_info(request)
    if request.method == "POST" or request.method == "PATCH":
        return create_general_client_info(request)
    if request.method == "DELETE":
        return delete_general_client_info(request)


@api_view(["GET", "PUT", "POST", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_equipment(request):
    if request.method == "GET":
        return get_equipment(request)
    if request.method == "PUT":
        return update_equipment(request)
    if request.method == "POST" or request.method == "PATCH":
        return create_equipment(request)
    if request.method == "DELETE":
        return delete_equipment(request)


@api_view(["GET", "PUT", "POST", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_program(request):
    if request.method == "GET":
        return get_program(request)
    if request.method == "PUT":
        return update_program(request)
    if request.method == "POST" or request.method == "PATCH":
        return create_program(request)
    if request.method == "DELETE":
        return delete_program(request)


@api_view(["GET", "PUT", "POST", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_power_endurance_assessment(request):
    if request.method == "GET":
        return get_power_endurance_assessment(request)
    if request.method == "PUT":
        return update_power_endurance_assessment(request)
    if request.method == "POST" or request.method == "PATCH":
        return create_power_endurance_assessment(request)
    if request.method == "DELETE":
        return delete_power_endurance_assessment(request)
