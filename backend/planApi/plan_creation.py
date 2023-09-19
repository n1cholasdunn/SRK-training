from gsheets.getters.get_training import get_otw_training
from planApi.models import TrainingExercise, OTWTrainingPlan


# print(get_otw_training())


def input_otw_plan():
    new_plan = OTWTrainingPlan.objects.create()
    data = get_otw_training()
    for entry in data:
        TrainingExercise.objects.create(
            training_plan=new_plan,
            name=entry[0],
            equipment_used=entry[1],
            rest=entry[2],
            sets=entry[3],
            notes=entry[4],
        )


input_otw_plan()
