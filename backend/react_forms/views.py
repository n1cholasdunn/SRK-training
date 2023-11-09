from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from react_forms.utils.climbing.oa_finger_strength import (
    create_oa_finger_strength_test,
    delete_oa_finger_strength_test,
    get_oa_finger_strength_test_by_id,
    get_oa_finger_strength_tests,
    update_oa_finger_strength_test,
)
from react_forms.utils.climbing.oa_pinch_strength import (
    create_oa_pinch_strength_test,
    delete_oa_pinch_strength_test,
    get_oa_pinch_strength_test_by_id,
    get_oa_pinch_strength_tests,
    update_oa_pinch_strength_test,
)
from react_forms.utils.climbing.finger_strength import (
    create_finger_strength_test,
    delete_finger_strength_test,
    get_finger_strength_test_by_id,
    get_finger_strength_tests,
    update_finger_strength_test,
)
from react_forms.utils.climbing.max_lockoff import (
    create_max_lockoff_test,
    delete_max_lockoff_test,
    get_max_lockoff_test_by_id,
    get_max_lockoff_tests,
    update_max_lockoff_test,
)
from react_forms.utils.client.equipment import (
    create_equipment,
    delete_equipment,
    get_equipment,
    get_equipment_by_id,
    update_equipment,
)
from react_forms.utils.client.general_client_info import (
    create_general_client_info,
    delete_general_client_info,
    get_general_client_info,
    get_general_client_info_by_id,
    update_general_client_info,
    update_general_client_info_by_id,
)

from react_forms.utils.client.availability import (
    create_availability,
    delete_availability,
    get_availabilities,
    get_availability_by_id,
    update_availability,
)

from react_forms.utils.client.program import (
    get_program,
    create_program,
    get_program_by_id,
    update_program,
    delete_program,
)


from react_forms.utils.climbing.power_endurance import (
    get_power_endurance_test_by_id,
    get_power_endurance_tests,
    create_power_endurance_test,
    update_power_endurance_test,
    delete_power_endurance_test,
)
from react_forms.utils.climbing.max_pullups import (
    get_max_pullups_test_by_id,
    get_max_pullups_tests,
    create_max_pullups_test,
    update_max_pullups_test,
    delete_max_pullups_test,
)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_availability(request, pk):
    if request.method == "GET":
        return get_availabilities(request)
    if request.method == "POST":
        return create_availability(request)
    if request.method == "PUT" or request.method == "PATCH":
        return update_availability(request)
    if request.method == "DELETE":
        return delete_availability(request)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def handle_availability_by_id(request, pk):
    if request.method == "GET":
        return get_availability_by_id(request, pk)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_general_client_info(request):
    if request.method == "GET":
        return get_general_client_info(request)
    if request.method == "POST":
        return create_general_client_info(request)
    if request.method == "PUT" or request.method == "PATCH":
        return update_general_client_info(request)
    if request.method == "DELETE":
        return delete_general_client_info(request)


# TODO make update pages for sierra to update individial users info if she wants/needs
@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAdminUser])
def handle_general_client_info_admin(request, pk):
    if request.method == "GET":
        return get_general_client_info_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_general_client_info_by_id(request, pk)
    if request.method == "DELETE":
        return delete_general_client_info(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_equipment(request):
    if request.method == "GET":
        return get_equipment(request)
    if request.method == "POST" or request.method == "PATCH":
        return create_equipment(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_equipment_by_id(request, pk):
    if request.method == "GET":
        return get_equipment_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_equipment(request, pk)
    if request.method == "DELETE":
        return delete_equipment(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_program(request):
    if request.method == "GET":
        return get_program(request)
    if request.method == "POST":
        return create_program(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_program_by_id(request, pk):
    if request.method == "GET":
        return get_program_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_program(request, pk)
    if request.method == "DELETE":
        return delete_program(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_power_endurance_test(request):
    if request.method == "GET":
        return get_power_endurance_tests(request)
    if request.method == "POST":
        return create_power_endurance_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_power_endurance_test_by_id(request, pk):
    if request.method == "GET":
        return get_power_endurance_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_power_endurance_test(request, pk)
    if request.method == "DELETE":
        return delete_power_endurance_test(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_max_pullups_test(request):
    if request.method == "GET":
        return get_max_pullups_tests(request)
    if request.method == "POST":
        return create_max_pullups_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_max_pullups_test_by_id(request, pk):
    if request.method == "GET":
        return get_max_pullups_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_max_pullups_test(request, pk)
    if request.method == "DELETE":
        return delete_max_pullups_test(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_max_lockoff_test(request):
    if request.method == "GET":
        return get_max_lockoff_tests(request)
    if request.method == "POST":
        return create_max_lockoff_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_max_lockoff_test_by_id(request, pk):
    if request.method == "GET":
        return get_max_lockoff_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_max_lockoff_test(request, pk)
    if request.method == "DELETE":
        return delete_max_lockoff_test(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_finger_strength_test(request):
    if request.method == "GET":
        return get_finger_strength_tests(request)
    if request.method == "POST":
        return create_finger_strength_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_finger_strength_test_by_id(request, pk):
    if request.method == "GET":
        return get_finger_strength_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_finger_strength_test(request, pk)
    if request.method == "DELETE":
        return delete_finger_strength_test(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_oa_finger_strength_test(request):
    if request.method == "GET":
        return get_oa_finger_strength_tests(request)
    if request.method == "POST":
        return create_oa_finger_strength_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_oa_finger_strength_test_by_id(request, pk):
    if request.method == "GET":
        return get_oa_finger_strength_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_oa_finger_strength_test(request, pk)
    if request.method == "DELETE":
        return delete_oa_finger_strength_test(request, pk)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def handle_oa_pinch_strength_test(request):
    if request.method == "GET":
        return get_oa_pinch_strength_tests(request)
    if request.method == "POST":
        return create_oa_pinch_strength_test(request)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def handle_oa_pinch_strength_test_by_id(request, pk):
    if request.method == "GET":
        return get_oa_pinch_strength_test_by_id(request, pk)
    if request.method == "PUT" or request.method == "PATCH":
        return update_oa_pinch_strength_test(request, pk)
    if request.method == "DELETE":
        return delete_oa_pinch_strength_test(request, pk)
