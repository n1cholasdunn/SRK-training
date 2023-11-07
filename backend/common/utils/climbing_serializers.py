from common.utils.base_serializer import BaseOwnerFieldSerializer
from common.models.climbing_models import (
    FingerStrengthTest,
    MaxLockoffTest,
    MaxPullupsTest,
    OAFingerStrengthTest,
    OAPinchTest,
    PowerEnduranceTest,
)
from rest_framework.serializers import ModelSerializer


class PowerEnduranceTestSerializer(ModelSerializer):
    class Meta:
        model = PowerEnduranceTest
        fields = "__all__"
        extra_kwargs = {
            "assessment": {"read_only": True},  # Add this line
        }


# class PowerEnduranceAssessmentsSerializer(BaseOwnerFieldSerializer):
#     tests = PowerEnduranceTestSerializer(many=True, required=False)

#     class Meta(BaseOwnerFieldSerializer.Meta):
#         model = PowerEnduranceAssessments
#         fields = "__all__"
#         extra_kwargs = {"trainee": {"read_only": True}}

#     def create(self, validated_data):
#         tests_data = validated_data.pop("tests", [])
#         assessment = PowerEnduranceAssessments.objects.create(**validated_data)
#         for test_data in tests_data:
#             PowerEnduranceTest.objects.create(assessment=assessment, **test_data)
#         return assessment


class MaxPullupsTestSerializer(ModelSerializer):
    class Meta:
        model = MaxPullupsTest
        fields = "__all__"


class MaxLockoffTestSerializer(ModelSerializer):
    class Meta:
        model = MaxLockoffTest
        fields = "__all__"


class FingerStrengthTestSerializer(ModelSerializer):
    class Meta:
        model = FingerStrengthTest
        fields = "__all__"


class OAFingerStrengthTestSerializer(ModelSerializer):
    class Meta:
        model = OAFingerStrengthTest
        fields = "__all__"


class OAPinchTestSerializer(ModelSerializer):
    class Meta:
        model = OAPinchTest
        fields = "__all__"
