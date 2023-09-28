from django.db import models
from core.models import User


# TODO Update plans to use Integer or Decimal Fields and alter formatting function to switch it up
class BaseTrainingPlan(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TrainingExercise(models.Model):
    training_plan = models.ForeignKey(
        "OTWTrainingPlan", related_name="exercises", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"


class OTWTrainingPlan(BaseTrainingPlan):
    warmup = models.TextField(null=True, blank=True)


class GymTrainingExercise(models.Model):
    training_plan = models.ForeignKey(
        "GymTrainingPlan", related_name="exercises", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"


class GymTrainingPlan(BaseTrainingPlan):
    pass


class PrehabTrainingExercise(models.Model):
    training_plan = models.ForeignKey(
        "PrehabTrainingPlan", related_name="exercises", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.equipment_used} - {self.rest} - {self.sets} - {self.notes}"


class PrehabTrainingPlan(BaseTrainingPlan):
    pass
