from rest_framework.response import Response
from rest_framework import status
from planApi.gsheets.getters.get_training import (
    get_otw_training,
    get_gym_training,
    get_prehab_training,
)
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


#!OTW
def get_otw_exercises(request, plan_id):
    exercises = TrainingExercise.objects.filter(training_plan_id=plan_id)
    serializer = TrainingExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def input_otw_plan(request):
    new_plan = OTWTrainingPlan.objects.create(trainee=request.user)
    data = get_otw_training()
    for entry in data:
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
    new_plan = GymTrainingPlan.objects.create(trainee=request.user)
    data = get_gym_training()
    for entry in data:
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
    new_plan = PrehabTrainingPlan.objects.create(trainee=request.user)
    data = get_prehab_training()
    for entry in data:
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
