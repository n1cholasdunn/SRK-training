from django.db import models
from core.models import User


class UserTimeStamp(models.Model):
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    trainee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class BaseClientInfo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
