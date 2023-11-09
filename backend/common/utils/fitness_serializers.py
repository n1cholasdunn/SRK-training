from re import S
from venv import create
from common.utils.base_serializer import BaseOwnerFieldSerializer
from rest_framework.serializers import ModelSerializer
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
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class MeasurementsTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = MeasurementsTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class OverheadSquatTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = OverheadSquatTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class YMCAStepTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = YMCAStepTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class SitReachTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = SitReachTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class PushUpTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = PushUpTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class DaviesTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = DaviesTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class SharkSkillsSideSerializer(ModelSerializer):
    class Meta:
        model = SharkSkillsSide
        fields = "__all__"


class SharkSkillsTestSerializer(BaseOwnerFieldSerializer):
    practice_left = SharkSkillsSideSerializer()
    practice_right = SharkSkillsSideSerializer()
    first_left = SharkSkillsSideSerializer()
    first_right = SharkSkillsSideSerializer()
    second_left = SharkSkillsSideSerializer()
    second_right = SharkSkillsSideSerializer()

    class Meta(BaseOwnerFieldSerializer.Meta):
        model = SharkSkillsTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}

    def create(self, validated_data):
        practice_left_data = validated_data.pop("practice_left")
        practice_right_data = validated_data.pop("practice_right")
        first_left_data = validated_data.pop("first_left")
        first_right_data = validated_data.pop("first_right")
        second_left_data = validated_data.pop("second_left")
        second_right_data = validated_data.pop("second_right")

        practice_left = SharkSkillsSide.objects.create(**practice_left_data)
        practice_right = SharkSkillsSide.objects.create(**practice_right_data)
        first_left = SharkSkillsSide.objects.create(**first_left_data)
        first_right = SharkSkillsSide.objects.create(**first_right_data)
        second_left = SharkSkillsSide.objects.create(**second_left_data)
        second_right = SharkSkillsSide.objects.create(**second_right_data)

        shark_skills_test = SharkSkillsTest.objects.create(
            practice_left=practice_left,
            practice_right=practice_right,
            first_left=first_left,
            first_right=first_right,
            second_left=second_left,
            second_right=second_right,
            **validated_data
        )

        return shark_skills_test


class CoreTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = CoreTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}
