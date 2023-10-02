from django.contrib import admin
from planApi.models.fitness_models import (
    HealthMarkersTest,
    HealthMarkersAssessments,
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
    SharkSkillsSide,
    SharkSkillsTest,
    CoreAssessments,
    CoreTest,
)


@admin.register(HealthMarkersTest)
class HealthMarkersTestAdmin(admin.ModelAdmin):
    list_display = [
        "weight",
        "bmi",
        "waist_hip_ratio",
        "resting_hr",
        "blood_pressure",
        "vo2_max",
    ]


@admin.register(HealthMarkersAssessments)
class HealthMarkersAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(MeasurementsTest)
class MeasurementsTestAdmin(admin.ModelAdmin):
    list_display = [
        "chest",
        "biceps",
        "forearms",
        "lower_abdomen",
        "hips",
        "upper_thigh",
        "mid_thigh",
        "calves",
    ]


@admin.register(MeasurementsAssessments)
class MeasurementsAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(OverheadSquatTest)
class OverheadSquatTestAdmin(admin.ModelAdmin):
    list_display = ["foot_ankle", "knee", "lphc", "shoulder", "solutions"]


@admin.register(OverheadSquatAssessments)
class OverheadSquatAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(SitReachTest)
class SitReachTestAdmin(admin.ModelAdmin):
    list_display = ["measurement"]


@admin.register(SitReachAssessments)
class SitReachAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(YMCAStepTest)
class YMCAStepTestAdmin(admin.ModelAdmin):
    list_display = ["recovery_hr", "rating"]


@admin.register(YMCAStepAssessments)
class YMCAStepAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(PushUpTest)
class PushUpTestAdmin(admin.ModelAdmin):
    list_display = ["num_pushups"]


@admin.register(PushUpAssessments)
class PushUpAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(DaviesTest)
class DaviesTestAdmin(admin.ModelAdmin):
    list_display = ["first_trial", "second_trial", "third_trial"]


@admin.register(DaviesAssessments)
class DaviesAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(SharkSkillsSide)
class SharkSkillsSideAdmin(admin.ModelAdmin):
    list_display = ["time", "deduction_tally", "total_deducted", "final_total"]


@admin.register(SharkSkillsTest)
class SharkSkillsTestAdmin(admin.ModelAdmin):
    list_display = [
        "practice_left",
        "practice_right",
        "first_left",
        "first_right",
        "second_left",
        "second_right",
    ]


@admin.register(SharkSkillsAssessments)
class SharkSkillsAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests


@admin.register(CoreTest)
class CoreTestAdmin(admin.ModelAdmin):
    list_display = ["first_trial", "second_trial"]


@admin.register(CoreAssessments)
class CoreAssessmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "test_list"]

    def test_list(self, obj):
        tests = obj.tests.all()
        return tests
