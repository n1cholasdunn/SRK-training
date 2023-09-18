from django.contrib import admin

from .models import OTWTrainingPlan

# Register your models here.


@admin.register(OTWTrainingPlan)
class OTWTrainingPlanAdmin(admin.ModelAdmin):
    list_display = ["exercise_count", "trainee", "warmup"]

    def exercise_count(self, obj):
        return obj.exercises.count()

    exercise_count.short_description = "Number of Exercises"
