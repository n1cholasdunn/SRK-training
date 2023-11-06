from common.models.climbing_models import (
    FingerStrengthAssessments,
    FingerStrengthTest,
    MaxLockoffAssessments,
    MaxLockoffTest,
    MaxPullupsAssessments,
    MaxPullupsTest,
    OAFingerStrengthAssessments,
    OAFingerStrengthTest,
    OAPinchAssessments,
    OAPinchTest,
    PowerEnduranceAssessments,
    PowerEnduranceTest,
)
from rest_framework.serializers import ModelSerializer


class PowerEnduranceTestSerializer(ModelSerializer):
    class Meta:
        model = PowerEnduranceTest
        fields = "__all__"


class PowerEnduranceAssessmentsSerializer(ModelSerializer):
    tests = PowerEnduranceTestSerializer(many=True, read_only=True)

    class Meta:
        model = PowerEnduranceAssessments
        fields = "__all__"


class MaxPullupsTestSerializer(ModelSerializer):
    class Meta:
        model = MaxPullupsTest
        fields = "__all__"


class MaxPullupsAssessmentsSerializer(ModelSerializer):
    tests = MaxPullupsTestSerializer(many=True, read_only=True)

    class Meta:
        model = MaxPullupsAssessments
        fields = "__all__"


class MaxLockoffTestSerializer(ModelSerializer):
    class Meta:
        model = MaxLockoffTest
        fields = "__all__"


class MaxLockoffAssessmentsSerializer(ModelSerializer):
    tests = MaxLockoffTestSerializer(many=True, read_only=True)

    class Meta:
        model = MaxLockoffAssessments
        fields = "__all__"


class FingerStrengthTestSerializer(ModelSerializer):
    class Meta:
        model = FingerStrengthTest
        fields = "__all__"


class FingerStrengthAssessmentsSerializer(ModelSerializer):
    tests = FingerStrengthTestSerializer(many=True, read_only=True)

    class Meta:
        model = FingerStrengthAssessments
        fields = "__all__"


class OAFingerStrengthTestSerializer(ModelSerializer):
    class Meta:
        model = OAFingerStrengthTest
        fields = "__all__"


class OAFingerStrengthAssessmentsSerializer(ModelSerializer):
    tests = OAFingerStrengthTestSerializer(many=True, read_only=True)

    class Meta:
        model = OAFingerStrengthAssessments
        fields = "__all__"


class OAPinchTestSerializer(ModelSerializer):
    class Meta:
        model = OAPinchTest
        fields = "__all__"


class OAPinchAssessmentsSerializer(ModelSerializer):
    tests = OAPinchTestSerializer(many=True, read_only=True)

    class Meta:
        model = OAPinchAssessments
        fields = "__all__"
