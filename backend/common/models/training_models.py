from django.db import models
from core.models import User
from common.models.common import UserTimeStamp


# TODO Update plans to use Integer or Decimal Fields and alter formatting function to switch it up


class OTWTrainingExercise(UserTimeStamp):
    warmup = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"


class GymTrainingExercise(UserTimeStamp):
    warmup = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"


class PrehabTrainingExercise(UserTimeStamp):
    warmup = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"
