from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from react_forms.utils.climbing.finger_strength import create_finger_strength_test
from react_forms.utils.climbing.max_lockoff import create_max_lockoff_test
from react_forms.utils.climbing.max_pullups import create_max_pullups_test
from react_forms.utils.climbing.power_endurance import create_power_endurance_test
from react_forms.utils.climbing.oa_finger_strength import create_oa_finger_strength_test
from react_forms.utils.climbing.oa_pinch_strength import create_oa_pinch_strength_test


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_multiple_tests(request):
    response_data = {}
    status_code = status.HTTP_200_OK

    if "power_endurance" in request.data:
        power_endurance_response = create_power_endurance_test(request)
        response_data["power_endurance"] = power_endurance_response.data
        if power_endurance_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "max_pullups" in request.data:
        max_pullups_response = create_max_pullups_test(request)
        response_data["max_pullups"] = max_pullups_response.data
        if max_pullups_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "max_lockoff" in request.data:
        max_lockoff_response = create_max_lockoff_test(request)
        response_data["max_lockoff"] = max_lockoff_response.data
        if max_lockoff_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "finger_strength" in request.data:
        finger_strength_response = create_finger_strength_test(request)
        response_data["finger_strength"] = finger_strength_response.data
        if finger_strength_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "oa_finger_strength" in request.data:
        oa_finger_strength_response = create_oa_finger_strength_test(request)
        response_data["oa_finger_strength"] = oa_finger_strength_response.data
        if oa_finger_strength_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "oa_pinch_strength" in request.data:
        oa_pinch_strength_response = create_oa_pinch_strength_test(request)
        response_data["oa_pinch_strength"] = oa_pinch_strength_response.data
        if oa_pinch_strength_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS
    flattened_data = {k: v[k]["tests"] for k, v in response_data.items() if k in v}
    return Response(flattened_data, status=status_code)
