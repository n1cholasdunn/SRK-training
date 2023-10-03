from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils.training_utils import (
    get_otw_exercises,
    input_otw_plan,
    update_otw_plan,
    delete_otw_plan,
    get_gym_exercises,
    input_gym_plan,
    delete_gym_plan,
    update_gym_plan,
    get_prehab_exercises,
    input_prehab_plan,
    update_prehab_plan,
    delete_prehab_plan,
)
from .utils.fitness_utils import (
    delete_health_markers_test,
    delete_measurements_assessments,
    delete_measurements_test,
    delete_overhead_squat_assessments,
    delete_overhead_squat_test,
    get_health_markers_test,
    get_measurements_assessments,
    get_measurements_test,
    get_overhead_squat_assessments,
    get_overhead_squat_test,
    input_health_markers_test,
    get_health_markers_assessments,
    delete_health_markers_assessments,
    input_measurements_test,
    input_overhead_squat_test,
    update_health_markers_test,
    update_measurements_test,
    update_overhead_squat_test,
)


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            # TODO update list of rotues once all models and data fetching/writing is complete
            "Endpoint": "/plans/otw/",
            "method": "GET",
            "body": None,
            "description": "Returns OTW training plans in descending order",
        },
        {
            "Endpoint": "/plans/otw/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new OTW training plan",
        },
        {
            "Endpoint": "/plans/otw/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing OTW training plan",
        },
        {
            "Endpoint": "/plans/otw/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes OTW existing training plan",
        },
        {
            "Endpoint": "/plans/gym/",
            "method": "GET",
            "body": None,
            "description": "Returns gym training plans in descending order",
        },
        {
            "Endpoint": "/plans/gym/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new gym training plan",
        },
        {
            "Endpoint": "/plans/gym/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing gym training plan",
        },
        {
            "Endpoint": "/plans/gym/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes gym existing training plan",
        },
        {
            "Endpoint": "/plans/prehab/",
            "method": "GET",
            "body": None,
            "description": "Returns prehab training plans in descending order",
        },
        {
            "Endpoint": "/plans/prehab/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new prehab training plan",
        },
        {
            "Endpoint": "/plans/prehab/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing prehab training plan",
        },
        {
            "Endpoint": "/plans/prehab/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes prehab existing training plan",
        },
    ]
    return Response(routes)


# TODO create a route for input plan from sheet to be unique and different from regular routes
# TODO Create route to input everything from a sheet like click which are filled out in a form and then have a route for different combinations of fitness/climbing assessments + plans
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_otw_input(request):
    return input_otw_plan(request)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_otw_plan(request, pk):
    if request.method == "GET":
        return get_otw_exercises(request, pk)
    if request.method == "PUT":
        return update_otw_plan(request, pk)
    if request.method == "DELETE":
        return delete_otw_plan(request, pk)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_gym_input(request):
    return input_gym_plan(request)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_gym_plan(request, pk):
    if request.method == "GET":
        return get_gym_exercises(request, pk)
    if request.method == "PUT":
        return update_gym_plan(request, pk)
    if request.method == "DELETE":
        return delete_gym_plan(request, pk)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_prehab_input(request):
    return input_prehab_plan(request)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_prehab_plan(request, pk):
    if request.method == "GET":
        return get_prehab_exercises(request, pk)
    if request.method == "PUT":
        return update_prehab_plan(request, pk)
    if request.method == "DELETE":
        return delete_prehab_plan(request, pk)


# Health Markers
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_health_markers_input(request):
    return input_health_markers_test(request)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_health_markers_assessments(request, pk):
    if request.method == "GET":
        return get_health_markers_assessments(request, pk)
    if request.method == "DELETE":
        return delete_health_markers_assessments(request, pk)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_health_markers_tests(request, pk):
    if request.method == "GET":
        return get_health_markers_test(request, pk)
    if request.method == "PUT":
        return update_health_markers_test(request, pk)
    if request.method == "DELETE":
        return delete_health_markers_test(request, pk)


# Measurements
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_measurements_input(request):
    return input_measurements_test(request)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_measurements_assessments(request, pk):
    if request.method == "GET":
        return get_measurements_assessments(request, pk)
    if request.method == "DELETE":
        return delete_measurements_assessments(request, pk)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_measurements_tests(request, pk):
    if request.method == "GET":
        return get_measurements_test(request, pk)
    if request.method == "PUT":
        return update_measurements_test(request, pk)
    if request.method == "DELETE":
        return delete_measurements_test(request, pk)


# overhead squats
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def handle_overhead_squat_input(request):
    return input_overhead_squat_test(request)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_overhead_squat_assessments(request, pk):
    if request.method == "GET":
        return get_overhead_squat_assessments(request, pk)
    if request.method == "DELETE":
        return delete_overhead_squat_assessments(request, pk)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_overhead_squat_tests(request, pk):
    if request.method == "GET":
        return get_overhead_squat_test(request, pk)
    if request.method == "PUT":
        return update_overhead_squat_test(request, pk)
    if request.method == "DELETE":
        return delete_overhead_squat_test(request, pk)
