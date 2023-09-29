from django.contrib import admin
from planApi.models.client_models import (
    GeneralClientInfo,
    DayAvailability,
    ClientAvailability,
    Equipment,
    ClientEquipment,
    ClientProgramInfo,
)


@admin.register(GeneralClientInfo)
class GeneralClientInfoAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "age",
        "email",
        "address",
        "emergency_contact",
        "emergency_phone",
    ]


@admin.register(DayAvailability)
class DayAvailabilityAdmin(admin.ModelAdmin):
    list_display = ["am", "pm"]


@admin.register(ClientAvailability)
class ClientAvailabilityAdmin(admin.ModelAdmin):
    list_display = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ClientEquipment)
class ClientEquipmentAdmin(admin.ModelAdmin):
    list_display = ["equipment"]


@admin.register(ClientProgramInfo)
class ClientProgramInfoAdmin(admin.ModelAdmin):
    list_display = [
        "program_type",
        "training_style",
        "payment_rate",
        "program_start",
        "outdoor_max",
        "outdoor_flash",
        "indoor_max",
        "indoor_flash",
    ]
