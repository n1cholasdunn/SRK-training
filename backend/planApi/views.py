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


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            # TODO add in userId after Oauth is added
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


# def input_otw_plan(request):
#     if request.method == "POST":
#         new_plan = OTWTrainingPlan.objects.create(trainee=request.user)
#         data = get_otw_training()
#         for entry in data:
#             exercise = TrainingExercise(
#                 training_plan=new_plan,
#                 name=entry[0],
#                 equipment_used=entry[1],
#                 rest=entry[2],
#                 sets=entry[3],
#                 notes=entry[4],
#             )
#             exercise.save()

#         return Response(
#             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
#         )


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# # def input_otw_plan_view(request):
# #     if request.method == "POST":
# #         new_plan = OTWTrainingPlan.objects.create(trainee=request.user)
# #         data = get_otw_training()
# #         for entry in data:
# #             exercise = TrainingExercise(
# #                 training_plan=new_plan,
# #                 name=entry[0],
# #                 equipment_used=entry[1],
# #                 rest=entry[2],
# #                 sets=entry[3],
# #                 notes=entry[4],
# #             )
# #             exercise.save()

# #         return Response(
# #             {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
# #         )


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_otw_exercises(request, pk):
#     if request.method == "GET":
#         exercises = TrainingExercise.objects.filter(training_pk=pk)
#         serializer = TrainingExerciseSerializer(exercises, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == "POST":
#         return input_otw_plan(request)
