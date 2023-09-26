from django.db import models
from .climbing_models import BaseAssessment


class HealthMarkersAssessments(BaseAssessment):
    pass


class HealthMarkerTest(models.Model):
    assessment = models.ForeignKey(
        "HealthMarkersAssessment", related_name="tests", on_delete=models.CASCADE
    )
    weight = models.CharField(max_length=10, null=True, blank=True)
    bmi = models.CharField(max_length=6, null=True, blank=True)
    waist_hip_ratio = models.CharField(max_length=6, null=True, blank=True)
    resting_hr = models.CharField(max_length=6, null=True, blank=True)
    blood_pressure = models.CharField(max_length=6, null=True, blank=True)
    vo2_max = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.weight} - {self.bmi} - {self.waist_hip_ratio} - {self.resting_hr} - {self.blood_pressure} - {self.vo2_max}"


class MeasurementsAssessments(BaseAssessment):
    pass


class MeasurementsTest(models.Model):
    assessment = models.ForeignKey(
        "MeasurementsAssessment", related_name="tests", on_delete=models.CASCADE
    )
    chest = models.CharField(max_length=6, null=True, blank=True)
    biceps = models.CharField(max_length=6, null=True, blank=True)
    forearms = models.CharField(max_length=6, null=True, blank=True)
    lower_abdomen = models.CharField(max_length=6, null=True, blank=True)
    hips = models.CharField(max_length=6, null=True, blank=True)
    upper_thigh = models.CharField(max_length=6, null=True, blank=True)
    mid_thigh = models.CharField(max_length=6, null=True, blank=True)
    calves = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.chest} - {self.biceps} - {self.forearms} - {self.lower_abdomen} - {self.hips} - {self.upper_thigh} - {self.mid_thigh} - {self.calves}"


class OverheadSquatAssessments(BaseAssessment):
    pass


class OverheadSquatTest(models.Model):
    assessment = models.ForeignKey(
        "OverheadSquatAssessment", related_name="tests", on_delete=models.CASCADE
    )
    foot_ankle = models.CharField(max_length=250, null=True, blank=True)
    knee = models.CharField(max_length=250, null=True, blank=True)
    lphc = models.CharField(max_length=250, null=True, blank=True)
    shoulder = models.CharField(max_length=250, null=True, blank=True)
    solutions = models.TextField(max_length=750, null=True, blank=True)

    def __str__(self):
        return f"{self.foot_ankle} - {self.knee} - {self.lphc} - {self.shoulder} - {self.solutions}"


class YMCAStepAssessments(BaseAssessment):
    pass


class YMCAStepTest(models.Model):
    assessment = models.ForeignKey(
        "YMCAStepAssessment", related_name="tests", on_delete=models.CASCADE
    )
    recovery_hr = models.CharField(max_length=6, null=True, blank=True)
    rating = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.recovery_hr} - {self.rating}"


class SitReachAssessments(BaseAssessment):
    pass


class SitReachTest(models.Model):
    assessment = models.ForeignKey(
        "SitReachAssessment", related_name="tests", on_delete=models.CASCADE
    )
    measurement = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.measurement}"


class PushUpAssessments(BaseAssessment):
    pass


class PushUpTest(models.Model):
    assessment = models.ForeignKey(
        "PushUpAssessment", related_name="tests", on_delete=models.CASCADE
    )
    num_pushups = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.num_pushups}"


class DaviesAssessments(BaseAssessment):
    pass


class DaviesTest(models.Model):
    assessment = models.ForeignKey(
        "DaviesAssessment", related_name="tests", on_delete=models.CASCADE
    )
    first_trial = models.CharField(max_length=6, null=True, blank=True)
    second_trial = models.CharField(max_length=6, null=True, blank=True)
    third_trial = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial} - {self.third_trial}"


class SharkSkillsAssessments(BaseAssessment):
    pass


# TODO complex model nesting when I get home
class SharkSkillsTest(models.Model):
    assessment = models.ForeignKey(
        "SharkSkillsAssessment", related_name="tests", on_delete=models.CASCADE
    )
    practice_left = models.CharField(max_length=6, null=True, blank=True)
    practice_right = models.CharField(max_length=6, null=True, blank=True)
    first_left = models.CharField(max_length=6, null=True, blank=True)
    first_right = models.CharField(max_length=6, null=True, blank=True)
    second_left = models.CharField(max_length=6, null=True, blank=True)
    second_right = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial} - {self.third_trial}"


class CoreAssessments(BaseAssessment):
    pass


class CoreTest(models.Model):
    assessment = models.ForeignKey(
        "CoreAssessment", related_name="tests", on_delete=models.CASCADE
    )
    first_trial = models.CharField(max_length=6, null=True, blank=True)
    second_trial = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial}"
