from django.shortcuts import get_object_or_404
from requests import Request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from react_forms.utils.fitness.overhead_squat import create_overhead_squat_test
from react_forms.utils.fitness.sit_reach import create_sit_reach_test
from react_forms.utils.fitness.ymca_step import create_ymca_step_test
from react_forms.utils.fitness.core import create_core_test
from react_forms.utils.fitness.pushup import create_pushup_test
from react_forms.utils.fitness.davies import create_davies_test
from react_forms.utils.fitness.health_markers import create_health_markers_test
from react_forms.utils.fitness.shark_skills import create_shark_skills_test
from react_forms.utils.fitness.measurements import create_measurements_test


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_multiple_fitness_tests(request: Request) -> Response:
    response_data = {}
    status_code = status.HTTP_200_OK

    if "core" in request.data:
        core_response = create_core_test(request)
        response_data["core"] = core_response.data
        if core_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "davies" in request.data:
        davies_response = create_davies_test(request)
        response_data["davies"] = davies_response.data
        if davies_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "pushup" in request.data:
        pushup_response = create_pushup_test(request)
        response_data["pushup"] = pushup_response.data
        if pushup_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "sit_reach" in request.data:
        sit_reach_response = create_sit_reach_test(request)
        response_data["sit_reach"] = sit_reach_response.data
        if sit_reach_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "health_markers" in request.data:
        health_markers_response = create_health_markers_test(request)
        response_data["health_markers"] = health_markers_response.data
        if health_markers_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "measurements" in request.data:
        measurements_response = create_measurements_test(request)
        response_data["measurements"] = measurements_response.data
        if measurements_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "ymca_step" in request.data:
        ymca_step_response = create_ymca_step_test(request)
        response_data["ymca_step"] = ymca_step_response.data
        if ymca_step_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "overhead_squat" in request.data:
        overhead_squat_response = create_overhead_squat_test(request)
        response_data["overhead_squat"] = overhead_squat_response.data
        if overhead_squat_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    if "shark_skills" in request.data:
        shark_skills_response = create_shark_skills_test(request)
        response_data["shark_skills"] = shark_skills_response.data
        if shark_skills_response.status_code != status.HTTP_201_CREATED:
            status_code = status.HTTP_207_MULTI_STATUS

    flattened_data = {k: v[k]["tests"] for k, v in response_data.items() if k in v}
    return Response(flattened_data, status=status_code)
