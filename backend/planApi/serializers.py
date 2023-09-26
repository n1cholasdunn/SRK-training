from rest_framework.serializers import ModelSerializer
from .models.training_models import (
    OTWTrainingPlan,
    TrainingExercise,
    GymTrainingPlan,
    GymTrainingExercise,
    PrehabTrainingExercise,
    PrehabTrainingPlan,
)

# from .models import (
#     Client,
#     PrehabPlan,
#     OTWTrainingPlan,
#     GymTrainingPlan,
#     FitnessAssessment,
#     ClimbingAssessment,
# )


class TrainingExerciseSerializer(ModelSerializer):
    class Meta:
        model = TrainingExercise
        fields = ["name", "equipment_used", "rest", "sets", "notes"]
        # fields = "__all__"


class OTWTrainingPlanSerializer(ModelSerializer):
    exercises = TrainingExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = OTWTrainingPlan
        fields = ("id", "exercises", "warmup")


class GymTrainingExerciseSerializer(ModelSerializer):
    class Meta:
        model = GymTrainingExercise
        fields = ["name", "equipment_used", "rest", "sets", "notes"]


class GymTrainingPlanSerializer(ModelSerializer):
    exercises = TrainingExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = GymTrainingPlan
        fields = ("id", "exercises")


class PrehabTrainingPlanSerializer(ModelSerializer):
    exercises = TrainingExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = PrehabTrainingPlan
        fields = ("id", "exercises")


class PrehabTrainingExerciseSerializer(ModelSerializer):
    class Meta:
        model = PrehabTrainingExercise
        fields = ["name", "equipment_used", "rest", "sets", "notes"]


# class ClientSerializer(ModelSerializer):
#     class Meta:
#         model = Client
#         fields = "__all__"


# class PrehabPlanSerializer(ModelSerializer):
#     class Meta:
#         model = PrehabPlan
#         fields = "__all__"


# class GymTrainingPlanSerializer(ModelSerializer):
#     class Meta:
#         model = GymTrainingPlan
#         fields = "__all__"


# class FitnessAssessmentSerializer(ModelSerializer):
#     class Meta:
#         model = FitnessAssessment
#         fields = "__all__"


# class ClimbingAssessmentSerializer(ModelSerializer):
#     class Meta:
#         model = ClimbingAssessment
#         fields = "__all__"
