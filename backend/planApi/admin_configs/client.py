from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
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
        "parq_complete",
        "liability_waiver",
        "availability_summary",
    ]

    def availability_summary(self, obj):
        # Fetch the related availability object
        availability = getattr(obj, "availability", None)
        if availability:
            day_availabilities = availability.dayavailability_set.all()

            avail_strings = [
                f"{day.day}: {self.format_slots(day.slots)}"
                for day in day_availabilities
            ]

            return mark_safe("<br>".join(avail_strings))
        return "No availability set"

    def format_slots(self, slots_json):
        if slots_json:
            return (
                format_html_join(
                    ", ",
                    "{} to {}",
                    ((slot["from_time"], slot["to_time"]) for slot in slots_json),
                )
                or "No slots"
            )
        return "No slots"

    availability_summary.short_description = "Availability Summary"


@admin.register(DayAvailability)
class DayAvailabilityAdmin(admin.ModelAdmin):
    list_display = ["am", "pm"]


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
