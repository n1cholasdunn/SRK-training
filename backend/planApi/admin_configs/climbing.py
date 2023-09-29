from django.contrib import admin
from planApi.models.climbing_models import (
    PowerEnduranceAssessments,
    PowerEnduranceTest,
    MaxLockoffAssessments,
    MaxLockoffTest,
    MaxPullupsAssessments,
    MaxPullupsTest,
    FingerStrengthAssessments,
    FingerStrengthTest,
    OAFingerStrengthAssessments,
    OAFingerStrengthTest,
    OAPinchAssessments,
    OAPinchTest,
)


@admin.register(PowerEnduranceTest)
class PowerEnduranceTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(PowerEnduranceAssessments)
class PowerEnduranceAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(MaxLockoffTest)
class MaxLockoffTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(MaxLockoffAssessments)
class MaxLockoffAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(MaxPullupsTest)
class MaxPullupsTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(MaxPullupsAssessments)
class MaxPullupsAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(FingerStrengthTest)
class FingerStrengthTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(FingerStrengthAssessments)
class FingerStrengthAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(OAFingerStrengthTest)
class OAFingerStrengthTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(OAFingerStrengthAssessments)
class OAFingerStrengthAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(OAPinchTest)
class OAPinchTestAdmin(admin.ModelAdmin):
    list_display = ["test"]


@admin.register(OAPinchAssessments)
class OAPinchAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests
