from django.shortcuts import render

# from google_sheets.utils.crud.fitness.core import (
#     delete_core_test,
#     get_core_test,
#     input_core_test,
#     update_core_test,
# )
# from google_sheets.utils.crud.fitness.davies import (
#     delete_davies_test,
#     get_davies_test,
#     input_davies_test,
#     update_davies_test,
# )
# from google_sheets.utils.crud.fitness.health_markers import (
#     delete_health_markers_test,
#     get_health_markers_test,
#     input_health_markers_test,
#     update_health_markers_test,
# )
# from google_sheets.utils.crud.fitness.measurements import (
#     delete_measurements_test,
#     get_measurements_test,
#     input_measurements_test,
#     update_measurements_test,
# )
# from google_sheets.utils.crud.fitness.overhead_squat import (
#     delete_overhead_squat_test,
#     get_overhead_squat_test,
#     input_overhead_squat_test,
#     update_overhead_squat_test,
# )
# from google_sheets.utils.crud.fitness.pushup import (
#     delete_pushup_test,
#     get_pushup_test,
#     input_pushup_test,
#     update_pushup_test,
# )
# from google_sheets.utils.crud.fitness.sit_reach import (
#     delete_sit_reach_test,
#     get_sit_reach_test,
#     input_sit_reach_test,
#     update_sit_reach_test,
# )
# from google_sheets.utils.crud.fitness.ymca_step import (
#     delete_ymca_step_test,
#     get_ymca_step_test,
#     input_ymca_step_test,
#     update_ymca_step_test,
# )
# from google_sheets.utils.crud.training.gym import (
#     delete_gym_plan,
#     get_gym_exercises,
#     input_gym_plan,
#     update_gym_plan,
# )
# from google_sheets.utils.crud.training.otw import (
#     delete_otw_plan,
#     get_otw_exercises,
#     input_otw_plan,
#     update_otw_plan,
# )
# from google_sheets.utils.crud.training.prehab import (
#     delete_prehab_plan,
#     get_prehab_exercises,
#     input_prehab_plan,
#     update_prehab_plan,
# )
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# from .utils.crud.fitness.shark_skills import (
#     get_shark_skills_test,
#     update_shark_skills_test,
#     input_shark_skills_test,
#     delete_shark_skills_test,
# )


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
    ]
    return Response(routes)


# TODO create a route for input plan from sheet to be unique and different from regular routes
# TODO Create route to input everything from a sheet like click which are filled out in a form and then have a route for different combinations of fitness/climbing assessments + plans


# TODO CREATE ALL/ UPDATE ALL ROUTE FROM SHEET
# TODO CREATE/Climbing stuff only
# TODO Create/Fitness only
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_otw_input(request):
#     return input_otw_plan(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_otw_plan(request, pk):
#     if request.method == "GET":
#         return get_otw_exercises(request, pk)
#     if request.method == "PUT":
#         return update_otw_plan(request, pk)
#     if request.method == "DELETE":
#         return delete_otw_plan(request, pk)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_gym_input(request):
#     return input_gym_plan(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_gym_plan(request, pk):
#     if request.method == "GET":
#         return get_gym_exercises(request, pk)
#     if request.method == "PUT":
#         return update_gym_plan(request, pk)
#     if request.method == "DELETE":
#         return delete_gym_plan(request, pk)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_prehab_input(request):
#     return input_prehab_plan(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_prehab_plan(request, pk):
#     if request.method == "GET":
#         return get_prehab_exercises(request, pk)
#     if request.method == "PUT":
#         return update_prehab_plan(request, pk)
#     if request.method == "DELETE":
#         return delete_prehab_plan(request, pk)


# # Health Markers
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_health_markers_input(request):
#     return input_health_markers_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_health_markers_tests(request, pk):
#     if request.method == "GET":
#         return get_health_markers_test(request, pk)
#     if request.method == "PUT":
#         return update_health_markers_test(request, pk)
#     if request.method == "DELETE":
#         return delete_health_markers_test(request, pk)


# # Measurements
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_measurements_input(request):
#     return input_measurements_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_measurements_tests(request, pk):
#     if request.method == "GET":
#         return get_measurements_test(request, pk)
#     if request.method == "PUT":
#         return update_measurements_test(request, pk)
#     if request.method == "DELETE":
#         return delete_measurements_test(request, pk)


# # overhead squats
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_overhead_squat_input(request):
#     return input_overhead_squat_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_overhead_squat_tests(request, pk):
#     if request.method == "GET":
#         return get_overhead_squat_test(request, pk)
#     if request.method == "PUT":
#         return update_overhead_squat_test(request, pk)
#     if request.method == "DELETE":
#         return delete_overhead_squat_test(request, pk)


# # YMCA Step Test
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_ymca_step_input(request):
#     return input_ymca_step_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_ymca_step_tests(request, pk):
#     if request.method == "GET":
#         return get_ymca_step_test(request, pk)
#     if request.method == "PUT":
#         return update_ymca_step_test(request, pk)
#     if request.method == "DELETE":
#         return delete_ymca_step_test(request, pk)


# # Sit & Reach
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_sit_reach_input(request):
#     return input_sit_reach_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_sit_reach_tests(request, pk):
#     if request.method == "GET":
#         return get_sit_reach_test(request, pk)
#     if request.method == "PUT":
#         return update_sit_reach_test(request, pk)
#     if request.method == "DELETE":
#         return delete_sit_reach_test(request, pk)


# # Pushups
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_pushup_input(request):
#     return input_pushup_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_pushup_tests(request, pk):
#     if request.method == "GET":
#         return get_pushup_test(request, pk)
#     if request.method == "PUT":
#         return update_pushup_test(request, pk)
#     if request.method == "DELETE":
#         return delete_pushup_test(request, pk)


# # Davies Test
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_davies_input(request):
#     return input_davies_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_davies_tests(request, pk):
#     if request.method == "GET":
#         return get_davies_test(request, pk)
#     if request.method == "PUT":
#         return update_davies_test(request, pk)
#     if request.method == "DELETE":
#         return delete_davies_test(request, pk)


# # Core
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_core_input(request):
#     return input_core_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_core_tests(request, pk):
#     if request.method == "GET":
#         return get_core_test(request, pk)
#     if request.method == "PUT":
#         return update_core_test(request, pk)
#     if request.method == "DELETE":
#         return delete_core_test(request, pk)


# # Shark Skills
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def handle_shark_skills_input(request):
#     return input_shark_skills_test(request)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def handle_shark_skills_tests(request, pk):
#     if request.method == "GET":
#         return get_shark_skills_test(request, pk)
#     if request.method == "PUT":
#         return update_shark_skills_test(request, pk)
#     if request.method == "DELETE":
#         return delete_shark_skills_test(request, pk)


# #
