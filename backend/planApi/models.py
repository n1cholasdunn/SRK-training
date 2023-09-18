from django.db import models
from core.models import User


# Create your models here.
class TrainingExercise(models.Model):
    training_plan = models.ForeignKey(
        "OTWTrainingPlan", related_name="exercises", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    equipment_used = models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    sets = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)


class BaseTrainingPlan(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.training_plan)


class OTWTrainingPlan(BaseTrainingPlan):
    warmup = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.training_plan


# class ClimbingAssessment(models.Model):
#     body = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]


# class FitnessAssessment(models.Model):
#     body = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]


# class GymTrainingPlan(models.Model):
#     body = models.TextField(null=True, blank=True)
#     functionalStrengthTraining = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]


# class PrehabPlan(models.Model):
#     body = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]


# class Client(models.Model):
#     client_name = models.CharField(max_length=50)
#     client_phone = models.CharField(max_length=15, unique=True)
#     client_age = models.CharField(max_length=10)
#     client_email = models.EmailField(unique=True)
#     client_address = models.TextField(max_length=60)
#     client_height = models.CharField(max_length=15)
#     client_weight = models.CharField(max_length=15)
#     client_ape_index = models.CharField(max_length=15)
#     client_occupation = models.CharField(max_length=15)
#     client_hobbies = models.TextField(max_length=200)
#     client_emergency_contact = models.CharField(max_length=50)
#     client_emergency_phone = models.CharField(max_length=15)
#     client_goals = models.TextField(max_length=400)
#     client_health_concerns = models.TextField(max_length=400)
#     client_parq_complete = models.CharField(max_length=5)
#     client_waiver = models.CharField(max_length=5)
