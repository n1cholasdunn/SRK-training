from rest_framework.response import Response
from rest_framework import status
from planApi.gsheets.getters.get_training import (
    get_otw_training,
    get_gym_training,
    get_prehab_training,
)
from planApi.gsheets.utils.fetch_by_url import fetch_url_data
from .models import (
    OTWTrainingPlan,
    TrainingExercise,
    GymTrainingPlan,
    PrehabTrainingPlan,
    GymTrainingExercise,
    PrehabTrainingExercise,
)
from .serializers import (
    TrainingExerciseSerializer,
    GymTrainingExerciseSerializer,
    PrehabTrainingExerciseSerializer,
)
import requests


#!OTW
def get_otw_exercises(request, plan_id):
    exercises = TrainingExercise.objects.filter(training_plan_id=plan_id)
    serializer = TrainingExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_otw_plan(request):
    if request.method == "POST":
        url = request.data.get("url")
        print(url)
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_otw_training)

        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_plan = OTWTrainingPlan.objects.create(trainee=request.user)

        for entry in data:  # Adjust as per the actual data format received
            notes_value = entry[4] if len(entry) > 4 else ""
            exercise = TrainingExercise(
                training_plan=new_plan,
                name=entry[0],
                equipment_used=entry[1],
                rest=entry[2],
                sets=entry[3],
                notes=notes_value,
            )
            exercise.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_otw_plan(request, plan_id):
    try:
        existing_plan = OTWTrainingPlan.objects.get(id=plan_id, trainee=request.user)
    except OTWTrainingPlan.DoesNotExist:
        return Response(
            {"message": "OTW Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    data = get_otw_training()

    existing_plan.trainingexercise_set.all().delete()

    for entry in data:
        notes_value = entry[4] if len(entry) > 4 else ""
        exercise = TrainingExercise(
            training_plan=existing_plan,
            name=entry[0],
            equipment_used=entry[1],
            rest=entry[2],
            sets=entry[3],
            notes=notes_value,
        )
        exercise.save()

    return Response(
        {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
    )


def delete_otw_plan(request, plan_id):
    try:
        existing_plan = OTWTrainingPlan.objects.get(id=plan_id, trainee=request.user)
        existing_plan.delete()
        return Response(
            {"message": "OTW Training Plan deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    except OTWTrainingPlan.DoesNotExist:
        return Response(
            {"message": "OTW Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )


# !GYM
def get_gym_exercises(request, plan_id):
    exercises = GymTrainingExercise.objects.filter(training_plan_id=plan_id)
    serializer = GymTrainingExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_gym_plan(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_gym_training)

        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_plan = OTWTrainingPlan.objects.create(trainee=request.user)

        for entry in data:  # Adjust as per the actual data format received
            notes_value = entry[4] if len(entry) > 4 else ""
            exercise = GymTrainingExercise(
                training_plan=new_plan,
                name=entry[0],
                equipment_used=entry[1],
                rest=entry[2],
                sets=entry[3],
                notes=notes_value,
            )
            exercise.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_gym_plan(request, plan_id):
    try:
        existing_plan = GymTrainingPlan.objects.get(id=plan_id, trainee=request.user)
    except GymTrainingPlan.DoesNotExist:
        return Response(
            {"message": "Gym Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    data = get_gym_training()

    existing_plan.gymtrainingexercise_set.all().delete()

    for entry in data:
        notes_value = entry[4] if len(entry) > 4 else ""
        exercise = GymTrainingExercise(
            training_plan=existing_plan,
            name=entry[0],
            equipment_used=entry[1],
            rest=entry[2],
            sets=entry[3],
            notes=notes_value,
        )
        exercise.save()

    return Response(
        {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
    )


def delete_gym_plan(request, plan_id):
    try:
        existing_plan = GymTrainingPlan.objects.get(id=plan_id, trainee=request.user)
        existing_plan.delete()
        return Response(
            {"message": "Gym Training Plan deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    except GymTrainingPlan.DoesNotExist:
        return Response(
            {"message": "Gym Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )


# !Prehab
def get_prehab_exercises(request, plan_id):
    exercises = PrehabTrainingExercise.objects.filter(training_plan_id=plan_id)
    serializer = PrehabTrainingExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_prehab_plan(request):
    if request.method == "POST":
        url = request.data.get("url")
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = fetch_url_data(url, get_otw_training)

        except requests.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from {url}: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_plan = PrehabTrainingPlan.objects.create(trainee=request.user)

        for entry in data:  # Adjust as per the actual data format received
            notes_value = entry[4] if len(entry) > 4 else ""
            exercise = PrehabTrainingExercise(
                training_plan=new_plan,
                name=entry[0],
                equipment_used=entry[1],
                rest=entry[2],
                sets=entry[3],
                notes=notes_value,
            )
            exercise.save()

        return Response(
            {"message": "Data inputted successfully!"}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


def update_prehab_plan(request, plan_id):
    try:
        existing_plan = PrehabTrainingPlan.objects.get(id=plan_id, trainee=request.user)
    except PrehabTrainingPlan.DoesNotExist:
        return Response(
            {"message": "Prehab Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    data = get_prehab_training()

    existing_plan.prehabtrainingexercise_set.all().delete()

    for entry in data:
        notes_value = entry[4] if len(entry) > 4 else ""
        exercise = TrainingExercise(
            training_plan=existing_plan,
            name=entry[0],
            equipment_used=entry[1],
            rest=entry[2],
            sets=entry[3],
            notes=notes_value,
        )
        exercise.save()

    return Response(
        {"message": "Data updated successfully!"}, status=status.HTTP_200_OK
    )


def delete_prehab_plan(request, plan_id):
    try:
        existing_plan = PrehabTrainingPlan.objects.get(id=plan_id, trainee=request.user)
        existing_plan.delete()
        return Response(
            {"message": "Prehab Training Plan deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    except PrehabTrainingPlan.DoesNotExist:
        return Response(
            {"message": "Prehab Training Plan not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
