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


class PowerEnduranceTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = PowerEnduranceTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class MaxPullupsTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = MaxPullupsTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class MaxLockoffTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = MaxLockoffTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class FingerStrengthTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = FingerStrengthTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class OAFingerStrengthTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = OAFingerStrengthTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}


class OAPinchTestSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = OAPinchTest
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}
