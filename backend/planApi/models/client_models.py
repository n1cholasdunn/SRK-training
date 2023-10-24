from django.db import models
from .common import BaseClientInfo

from phonenumber_field.modelfields import PhoneNumberField  # type:ignore


class GeneralClientInfo(BaseClientInfo):
    name = models.CharField(max_length=75)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255)
    emergency_phone = models.CharField(max_length=255)
    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    ape_index = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    primary_goals = models.CharField(max_length=255)
    health_concerns = models.CharField(max_length=255, null=True, blank=True)
    parq_complete = models.BooleanField(default=False)
    liability_waiver = models.BooleanField(default=False)


class DayAvailability(models.Model):
    am = models.CharField(max_length=25, null=True, blank=True)
    pm = models.CharField(max_length=25, null=True, blank=True)


class ClientAvailability(BaseClientInfo):
    monday = models.ForeignKey(
        DayAvailability,
        related_name="monday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tuesday = models.ForeignKey(
        DayAvailability,
        related_name="tuesday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    wednesday = models.ForeignKey(
        DayAvailability,
        related_name="wednesday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    thursday = models.ForeignKey(
        DayAvailability,
        related_name="thursday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    friday = models.ForeignKey(
        DayAvailability,
        related_name="friday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    saturday = models.ForeignKey(
        DayAvailability,
        related_name="saturday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    sunday = models.ForeignKey(
        DayAvailability,
        related_name="sunday_availability",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class Equipment(models.Model):
    name = models.CharField(max_length=50)


class ClientEquipment(BaseClientInfo):
    equipment = models.ForeignKey(
        Equipment,
        related_name="client_equipment",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class ClientProgramInfo(BaseClientInfo):
    program_type = models.CharField(max_length=30)
    training_style = models.CharField(max_length=30)
    payment_rate = models.CharField(max_length=25)
    program_start = models.CharField(max_length=25, blank=True, null=True)
    outdoor_max = models.CharField(max_length=5, null=True, blank=True)
    outdoor_flash = models.CharField(max_length=5, null=True, blank=True)
    indoor_max = models.CharField(max_length=5, null=True, blank=True)
    indoor_flash = models.CharField(max_length=5, null=True, blank=True)
