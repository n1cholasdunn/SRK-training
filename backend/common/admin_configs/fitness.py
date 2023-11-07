from django.contrib import admin
from common.models.fitness_models import (
    HealthMarkersTest,
    MeasurementsTest,
    OverheadSquatTest,
    YMCAStepTest,
    SitReachTest,
    PushUpTest,
    DaviesTest,
    SharkSkillsSide,
    SharkSkillsTest,
    CoreTest,
)


@admin.register(HealthMarkersTest)
class HealthMarkersTestAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "weight",
        "bmi",
        "waist_hip_ratio",
        "resting_hr",
        "blood_pressure",
        "vo2_max",
    ]


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


@admin.register(OverheadSquatTest)
class OverheadSquatTestAdmin(admin.ModelAdmin):
    list_display = ["foot_ankle", "knee", "lphc", "shoulder", "solutions"]


@admin.register(SitReachTest)
class SitReachTestAdmin(admin.ModelAdmin):
    list_display = ["first_measurement", "second_measurement", "third_measurement"]


@admin.register(YMCAStepTest)
class YMCAStepTestAdmin(admin.ModelAdmin):
    list_display = ["recovery_hr", "rating"]


@admin.register(PushUpTest)
class PushUpTestAdmin(admin.ModelAdmin):
    list_display = ["num_pushups", "completed"]


@admin.register(DaviesTest)
class DaviesTestAdmin(admin.ModelAdmin):
    list_display = ["first_trial", "second_trial", "third_trial"]


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


@admin.register(CoreTest)
class CoreTestAdmin(admin.ModelAdmin):
    list_display = ["first_trial", "second_trial"]
