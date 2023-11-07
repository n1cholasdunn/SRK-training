from django.db import models
from django.db.models import JSONField
from .common import BaseClientInfo

from phonenumber_field.modelfields import PhoneNumberField  # type:ignore


class GeneralClientInfo(BaseClientInfo):
    name = models.CharField(max_length=75)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    age = models.IntegerField(null=False, blank=False)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255)
    emergency_phone = models.CharField(max_length=255)
    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    ape_index = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    primary_goals = models.CharField(max_length=255)
    health_concerns = models.CharField(max_length=255, null=True, blank=True)
    parq_complete = models.BooleanField(default=False)
    liability_waiver = models.BooleanField(default=False)


# TODO fix client availability to fit the format by supplying a day as well
class DayAvailability(models.Model):
    client = models.ForeignKey(
        GeneralClientInfo,
        on_delete=models.CASCADE,
        related_name="availabilities",
        null=True,
    )
    day = models.CharField(max_length=10, null=True)
    slots = JSONField(null=True, blank=True)
    am = models.CharField(max_length=25, null=True, blank=True)
    pm = models.CharField(max_length=25, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.day} - {self.client.name}"

    class Meta:
        unique_together = ("client", "day")
        # ensures one  availability per day


class ClientAvailability(models.Model):
    client = models.OneToOneField(
        GeneralClientInfo,
        on_delete=models.CASCADE,
        related_name="availability",
        null=True,
    )

    def __str__(self):
        return f"Availability for {self.client.name}"


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
    # TODO convert to integer in getter or just numbers in a string then coerce in frontend
    payment_rate = models.CharField(max_length=25)
    program_start = models.CharField(max_length=25, blank=True, null=True)
    outdoor_max = models.CharField(max_length=5, null=True, blank=True)
    outdoor_flash = models.CharField(max_length=5, null=True, blank=True)
    indoor_max = models.CharField(max_length=5, null=True, blank=True)
    indoor_flash = models.CharField(max_length=5, null=True, blank=True)
