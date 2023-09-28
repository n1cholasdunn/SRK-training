from django.db import models
from core.models import User


class BaseAssessment(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BaseClientInfo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
