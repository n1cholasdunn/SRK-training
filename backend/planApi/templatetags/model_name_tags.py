from django import template

register = template.Library()


@register.simple_tag
def get_model_lists():
    return {
        "climbing_assessment_names": [
            "PowerEnduranceAssessments",
            "MaxPullupsAssessments",
            "MaxLockoffAssessments",
            "FingerStrengthAssessments",
            "OAFingerStrengthAssessments",
            "OAPinchAssessments",
        ],
        "climbing_test_names": [
            "PowerEnduranceTest",
            "MaxPullupsTest",
            "MaxLockoffTest",
            "FingerStrengthTest",
            "OAFingerStrengthTest",
            "OAPinchTest",
        ],
        "fitness_assessment_names": [
            "HealthMarkersAssessments",
            "MeasurementsAssessments",
            "OverheadSquatAssessments",
            "YMCAStepAssessments",
            "SitReachAssessments",
            "PushupAssessments",
            "DaviesAssessments",
            "SharkSkillAssessments",
            "CoreAssessments",
        ],
        "fitness_test_names": [
            "HealthMarkersTest",
            "MeasurementsTest",
            "OverheadSquatTest",
            "YMCAStepTest",
            "SitReachTest",
            "PushupTest",
            "DaviesTest",
            "SharkSkillsTest",
            "CoreTest",
        ],
        "client_info_models": [
            "GeneralClientInfo",
            "DayAvailability",
            "ClientAvailability",
            "Equipment",
            "ClientEquipment",
            "ClientProgramInfo",
        ],
        "climbing_training_models": ["TrainingExercises", "OTWTrainingPlan"],
        "gym_training_models": ["GymTrainingExercise", "GymTrainingPlan"],
        "prehab_training_models": ["PrehabTrainingExercise", "PrehabTrainingPlan"],
    }


print("this is indeed loading")
