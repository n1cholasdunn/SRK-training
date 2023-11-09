from common.utils.base_serializer import BaseOwnerFieldSerializer
from common.models.fitness_models import (
    HealthMarkersTest,
    MeasurementsTest,
    OverheadSquatTest,
    YMCAStepTest,
    SitReachTest,
    PushUpTest,
    DaviesTest,
    SharkSkillsTest,
    SharkSkillsSide,
    CoreTest,
)


class HealthMarkersTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = HealthMarkersTest
        fields = [
            "weight",
            "bmi",
            "waist_hip_ratio",
            "resting_hr",
            "blood_pressure",
            "vo2_max",
        ]
        extra_kwargs = {"trainee": {"read_only": True}}


class MeasurementsTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
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
        extra_kwargs = {"trainee": {"read_only": True}}


class OverheadSquatTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = OverheadSquatTest
        fields = ["foot_ankle", "knee", "lphc", "shoulder", "solutions"]
        extra_kwargs = {"trainee": {"read_only": True}}


class YMCAStepTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = YMCAStepTest
        fields = ["recovery_hr", "rating"]
        extra_kwargs = {"trainee": {"read_only": True}}


class SitReachTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = SitReachTest
        fields = ["measurement"]
        extra_kwargs = {"trainee": {"read_only": True}}


class PushUpTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = PushUpTest
        fields = ["num_pushups"]
        extra_kwargs = {"trainee": {"read_only": True}}


class DaviesTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = DaviesTest
        fields = ["first_trial", "second_trial", "third_trial"]
        extra_kwargs = {"trainee": {"read_only": True}}


class SharkSkillsSideSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = SharkSkillsSide
        fields = ["time", "deduction_tally", "total_deducted", "final_total"]


class SharkSkillsTestSerializer(BaseOwnerFieldSerializer):
    practice_left = SharkSkillsSideSerializer(read_only=True)
    practice_right = SharkSkillsSideSerializer(read_only=True)
    first_left = SharkSkillsSideSerializer(read_only=True)
    first_right = SharkSkillsSideSerializer(read_only=True)
    second_left = SharkSkillsSideSerializer(read_only=True)
    second_right = SharkSkillsSideSerializer(read_only=True)

    class Meta(BaseOwnerFieldSerializer.Meta):
        model = SharkSkillsTest
        fields = [
            "practice_left",
            "practice_right",
            "first_left",
            "first_right",
            "second_left",
            "second_right",
        ]
        extra_kwargs = {"trainee": {"read_only": True}}


class CoreTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = CoreTest
        fields = ["first_trial", "second_trial"]
        extra_kwargs = {"trainee": {"read_only": True}}
