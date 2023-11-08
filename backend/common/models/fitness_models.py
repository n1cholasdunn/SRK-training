from django.db import models
from .common import UserTimeStamp


# TODO format data to be integers and floats to be stored in DB properly and have forms be reusable for react forms


class HealthMarkersTest(UserTimeStamp):
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    bmi = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    waist_hip_ratio = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    resting_hr = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    blood_pressure = models.CharField(max_length=30, null=True, blank=True)
    vo2_max = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f"{self.weight} - {self.bmi} - {self.waist_hip_ratio} - {self.resting_hr} - {self.blood_pressure} - {self.vo2_max}"


class MeasurementsTest(UserTimeStamp):
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


class OverheadSquatTest(UserTimeStamp):
    foot_ankle = models.CharField(max_length=250, null=True, blank=True)
    knee = models.CharField(max_length=250, null=True, blank=True)
    lphc = models.CharField(max_length=250, null=True, blank=True)
    shoulder = models.CharField(max_length=250, null=True, blank=True)
    solutions = models.TextField(max_length=750, null=True, blank=True)

    def __str__(self):
        return f"{self.foot_ankle} - {self.knee} - {self.lphc} - {self.shoulder} - {self.solutions}"


class YMCAStepTest(UserTimeStamp):
    recovery_hr = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    rating = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.recovery_hr} - {self.rating}"


class SitReachTest(UserTimeStamp):
    first_measurement = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    second_measurement = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    third_measurement = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_measurement - {self.second_measurement} - {self.third_measurement}}"


class PushUpTest(UserTimeStamp):
    num_pushups = models.IntegerField(null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f"{self.num_pushups}"


class DaviesTest(UserTimeStamp):
    first_trial = models.IntegerField(null=True, blank=True)
    second_trial = models.IntegerField(null=True, blank=True)
    third_trial = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial} - {self.third_trial}"


class SharkSkillsSide(UserTimeStamp):
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


class SharkSkillsTest(UserTimeStamp):
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


# TODO convert to seconds in fetch call and save in second format of intergers
class CoreTest(UserTimeStamp):
    first_trial = models.CharField(max_length=6, null=True, blank=True)
    second_trial = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.first_trial} - {self.second_trial}"
