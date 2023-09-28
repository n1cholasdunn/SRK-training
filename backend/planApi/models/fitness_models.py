from django.db import models
from .common import BaseAssessment


# TODO format data to be integers and floats to be stored in DB properly and have forms be reusable for react forms
class HealthMarkersAssessments(BaseAssessment):
    pass


class HealthMarkerTest(models.Model):
    assessment = models.ForeignKey(
        "HealthMarkersAssessments", related_name="tests", on_delete=models.CASCADE
    )
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    bmi = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    waist_hip_ratio = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    resting_hr = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    blood_pressure = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    vo2_max = models.DecimalField(decimal_places=2, max_digits=2, null=True, blank=True)

    def __str__(self):
        return f"{self.weight} - {self.bmi} - {self.waist_hip_ratio} - {self.resting_hr} - {self.blood_pressure} - {self.vo2_max}"


class MeasurementsAssessments(BaseAssessment):
    pass


class MeasurementsTest(models.Model):
    assessment = models.ForeignKey(
        "MeasurementsAssessments", related_name="tests", on_delete=models.CASCADE
    )
    chest = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    biceps = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    forearms = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    lower_abdomen = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    hips = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    upper_thigh = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    mid_thigh = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    calves = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f"{self.chest} - {self.biceps} - {self.forearms} - {self.lower_abdomen} - {self.hips} - {self.upper_thigh} - {self.mid_thigh} - {self.calves}"


class OverheadSquatAssessments(BaseAssessment):
    pass


class OverheadSquatTest(models.Model):
    assessment = models.ForeignKey(
        "OverheadSquatAssessments", related_name="tests", on_delete=models.CASCADE
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
        "YMCAStepAssessments", related_name="tests", on_delete=models.CASCADE
    )
    recovery_hr = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    rating = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.recovery_hr} - {self.rating}"


class SitReachAssessments(BaseAssessment):
    pass


class SitReachTest(models.Model):
    assessment = models.ForeignKey(
        "SitReachAssessments", related_name="tests", on_delete=models.CASCADE
    )
    measurement = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return f"{self.measurement}"


class PushUpAssessments(BaseAssessment):
    pass


class PushUpTest(models.Model):
    assessment = models.ForeignKey(
        "PushUpAssessments", related_name="tests", on_delete=models.CASCADE
    )
    num_pushups = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.num_pushups}"


class DaviesAssessments(BaseAssessment):
    pass


class DaviesTest(models.Model):
    assessment = models.ForeignKey(
        "DaviesAssessments", related_name="tests", on_delete=models.CASCADE
    )
    first_trial = models.IntegerField(null=True, blank=True)
    second_trial = models.IntegerField(null=True, blank=True)
    third_trial = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial} - {self.third_trial}"


class SharkSkillsAssessments(BaseAssessment):
    pass


class SharkSkillsSide(models.Model):
    time = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    deduction_tally = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    total_deducted = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    final_total = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )


class SharkSkillsTest(models.Model):
    assessment = models.ForeignKey(
        "SharkSkillsAssessments", related_name="tests", on_delete=models.CASCADE
    )
    practice_left = models.ForeignKey(
        SharkSkillsSide,
        related_name="practice_lefts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    practice_right = models.ForeignKey(
        SharkSkillsSide,
        related_name="practice_rights",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    first_left = models.ForeignKey(
        SharkSkillsSide,
        related_name="first_lefts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    first_right = models.ForeignKey(
        SharkSkillsSide,
        related_name="first_rights",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    second_left = models.ForeignKey(
        SharkSkillsSide,
        related_name="second_lefts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    second_right = models.ForeignKey(
        SharkSkillsSide,
        related_name="second_rights",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.practice_left} - {self.practice_right} - {self.first_left} - {self.first_right} - {self.second_left} - {self.second_right}"


class CoreAssessments(BaseAssessment):
    pass


class CoreTest(models.Model):
    assessment = models.ForeignKey(
        "CoreAssessments", related_name="tests", on_delete=models.CASCADE
    )
    first_trial = models.CharField(max_length=6, null=True, blank=True)
    second_trial = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial}"
