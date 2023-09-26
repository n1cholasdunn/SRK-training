from django.db import models
from .climbing_models import BaseAssessment


class HealthMarkersAssessment(BaseAssessment):
    pass


class HealthMarkerTests(models.Model):
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
        return f"{self.chest} - {self.biceps} - {self.forearms} - {self.lower_abdomen} - {self.hips} - {self.upper_thigh} - {self.mid_thigh} - {self.calves}"


class MeasurementsAssessment(BaseAssessment):
    pass


class MeasurementsTests(models.Model):
    # TODO how to make it limited to 10 or 11 entries
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
