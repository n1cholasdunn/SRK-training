from rest_framework.response import Response
from rest_framework import status
from planApi.gsheets.getters.get_training import get_otw_training
from .models import OTWTrainingPlan, TrainingExercise
from .serializers import OTWTrainingPlanSerializer


def get_otw_plans_list(request):
    plans = OTWTrainingPlan.objects.all().order_by("-updated")
    serializer = OTWTrainingPlanSerializer(plans, many=True)
    return Response(serializer.data)


def create_otw_plan(request):
    data = request.data
    plan = OTWTrainingPlan.objects.create(body=data["body"])
    serializer = OTWTrainingPlanSerializer(plan, many=False)
    return Response(serializer.data)


def get_otw_plan_detail(request, pk):
    plans = OTWTrainingPlan.objects.get(id=pk)
    serializer = OTWTrainingPlanSerializer(plans, many=False)
    return Response(serializer.data)


def update_otw_plan(request, pk):
    data = request.data
    plan = OTWTrainingPlan.objects.get(id=pk)
    serializer = OTWTrainingPlanSerializer(instance=plan, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def delete_otw_plan(request, pk):
    plan = OTWTrainingPlan.objects.get(id=pk)
    plan.delete()
    return Response("OTW Plan was deleted!")


# def input_otw_plan_view(request):
#     if request.method == "POST":
#         new_plan = OTWTrainingPlan.objects.create()
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
