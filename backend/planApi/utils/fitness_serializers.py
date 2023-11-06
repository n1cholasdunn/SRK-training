from rest_framework.serializers import ModelSerializer
from planApi.models.fitness_models import (
    HealthMarkersAssessments,
    HealthMarkersTest,
    MeasurementsAssessments,
    MeasurementsTest,
    OverheadSquatAssessments,
    OverheadSquatTest,
    YMCAStepAssessments,
    YMCAStepTest,
    SitReachAssessments,
    SitReachTest,
    PushUpAssessments,
    PushUpTest,
    DaviesAssessments,
    DaviesTest,
    SharkSkillsAssessments,
    SharkSkillsTest,
    SharkSkillsSide,
    CoreAssessments,
    CoreTest,
)


class HealthMarkersTestSerializer(ModelSerializer):
    class Meta:
        model = HealthMarkersTest
        fields = [
            "weight",
            "bmi",
            "waist_hip_ratio",
            "resting_hr",
            "blood_pressure",
            "vo2_max",
        ]


class HealthMarkersAssessmentsSerializer(ModelSerializer):
    tests = HealthMarkersTestSerializer(many=True, read_only=True)

    class Meta:
        model = HealthMarkersAssessments
        fields = ["id", "tests"]


class MeasurementsTestSerializer(ModelSerializer):
    class Meta:
        model = MeasurementsTest
        fields = [
            "chest",
            "biceps",
            "forearms",
            "lower_abdomen",
            "hips",
            "upper_thigh",
            "mid_thigh",
            "calves",
        ]


class MeasurementsAssessmentsSerializer(ModelSerializer):
    tests = MeasurementsTestSerializer(many=True, read_only=True)

    class Meta:
        model = MeasurementsAssessments
        fields = ["id", "assessments"]


class OverheadSquatTestSerializer(ModelSerializer):
    class Meta:
        model = OverheadSquatTest
        fields = ["foot_ankle", "knee", "lphc", "shoulder", "solutions"]


class OverheadSquatAssessmentsSerializer(ModelSerializer):
    tests = OverheadSquatTestSerializer(many=True, read_only=True)

    class Meta:
        model = OverheadSquatAssessments
        fields = ["id", "assessments"]


class YMCAStepTestSerializer(ModelSerializer):
    class Meta:
        model = YMCAStepTest
        fields = ["recovery_hr", "rating"]


class YMCAStepAssessmentsSerializer(ModelSerializer):
    tests = YMCAStepTestSerializer(many=True, read_only=True)

    class Meta:
        model = YMCAStepAssessments
        fields = ["id", "assessments"]


class SitReachTestSerializer(ModelSerializer):
    class Meta:
        model = SitReachTest
        fields = ["measurement"]


class SitReachAssessmentsSerializer(ModelSerializer):
    tests = SitReachTestSerializer(many=True, read_only=True)

    class Meta:
        model = SitReachAssessments
        fields = ["id", "assessments"]


class PushUpTestSerializer(ModelSerializer):
    class Meta:
        model = PushUpTest
        fields = ["num_pushups"]


class PushUpAssessmentsSerializer(ModelSerializer):
    tests = PushUpTestSerializer(many=True, read_only=True)

    class Meta:
        model = PushUpAssessments
        fields = ["id", "assessments"]


class DaviesTestSerializer(ModelSerializer):
    class Meta:
        model = DaviesTest
        fields = ["first_trial", "second_trial", "third_trial"]


class DaviesAssessmentsSerializer(ModelSerializer):
    tests = DaviesTestSerializer(many=True, read_only=True)

    class Meta:
        model = DaviesAssessments
        fields = ["id", "assessments"]


class SharkSkillsSideSerializer(ModelSerializer):
    class Meta:
        model = SharkSkillsSide
        fields = ["time", "deduction_tally", "total_deducted", "final_total"]


class SharkSkillsTestSerializer(ModelSerializer):
    practice_left = SharkSkillsSideSerializer(read_only=True)
    practice_right = SharkSkillsSideSerializer(read_only=True)
    first_left = SharkSkillsSideSerializer(read_only=True)
    first_right = SharkSkillsSideSerializer(read_only=True)
    second_left = SharkSkillsSideSerializer(read_only=True)
    second_right = SharkSkillsSideSerializer(read_only=True)

    class Meta:
        model = SharkSkillsTest
        fields = [
            "practice_left",
            "practice_right",
            "first_left",
            "first_right",
            "second_left",
            "second_right",
        ]


class SharkSkillsAssessmentsSerializer(ModelSerializer):
    tests = SharkSkillsTestSerializer(many=True, read_only=True)

    class Meta:
        model = SharkSkillsAssessments
        fields = ["id", "assessments"]


class CoreTestSerializer(ModelSerializer):
    class Meta:
        model = CoreTest
        fields = ["first_trial", "second_trial"]


class CoreAssessmentsSerializer(ModelSerializer):
    tests = CoreTestSerializer(many=True, read_only=True)

    class Meta:
        model = CoreAssessments
        fields = ["id", "assessments"]
