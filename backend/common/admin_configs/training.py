from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html_join

from common.models.training_models import (
    OTWTrainingPlan,
    TrainingExercise,
    GymTrainingExercise,
    GymTrainingPlan,
    PrehabTrainingExercise,
    PrehabTrainingPlan,
)


# Register your models here.
@admin.register(TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ["name", "equipment_used", "rest", "sets", "notes"]


@admin.register(OTWTrainingPlan)
class OTWTrainingPlanAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "exercise_count",
        "trainee",
        "warmup",
        "exercise_list",
        "created",
        "updated",
    ]

    def exercise_count(self, obj):
        return obj.exercises.count()

    def exercise_list(self, obj):
        # Get all related exercises and join their names using a comma
        exercises = obj.exercises.all()
        return ", ".join([exercise.name for exercise in exercises])

    def get_exercises(self, obj):
        # Get all related exercises
        exercises = obj.exercises.all()

        # Create a link to each exercise's change page in the admin
        return format_html_join(
            ", ",
            '<a href="{}">{}</a>',
            (
                (
                    # reverse(
                    #     "admin:common_trainingexercise_change", args=[exercise.pk]
                    # ),
                    reverse(
                        "admin:%s_%s_change"
                        % (exercise._meta.app_label, exercise._meta.model_name),
                        args=[exercise.pk],
                    ),
                    str(exercise),
                )
                for exercise in exercises
            ),
        )

    get_exercises.short_description = "Exercises"
    exercise_list.short_description = "Exercise Names"
    exercise_count.short_description = "Number of Exercises"


@admin.register(GymTrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ["name", "equipment_used", "rest", "sets", "notes"]


@admin.register(GymTrainingPlan)
class OTWTrainingPlanAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "exercise_count",
        "trainee",
        "exercise_list",
        "created",
        "updated",
    ]

    def exercise_count(self, obj):
        return obj.exercises.count()

    def exercise_list(self, obj):
        # Get all related exercises and join their names using a comma
        exercises = obj.exercises.all()
        return ", ".join([exercise.name for exercise in exercises])

    def get_exercises(self, obj):
        # Get all related exercises
        exercises = obj.exercises.all()

        # Create a link to each exercise's change page in the admin
        return format_html_join(
            ", ",
            '<a href="{}">{}</a>',
            (
                (
                    # reverse(
                    #     "admin:common_trainingexercise_change", args=[exercise.pk]
                    # ),
                    reverse(
                        "admin:%s_%s_change"
                        % (exercise._meta.app_label, exercise._meta.model_name),
                        args=[exercise.pk],
                    ),
                    str(exercise),
                )
                for exercise in exercises
            ),
        )

    get_exercises.short_description = "Exercises"
    exercise_list.short_description = "Exercise Names"
    exercise_count.short_description = "Number of Exercises"


@admin.register(PrehabTrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ["name", "equipment_used", "rest", "sets", "notes"]


@admin.register(PrehabTrainingPlan)
class OTWTrainingPlanAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "exercise_count",
        "trainee",
        "exercise_list",
        "created",
        "updated",
    ]

    def exercise_count(self, obj):
        return obj.exercises.count()

    def exercise_list(self, obj):
        # Get all related exercises and join their names using a comma
        exercises = obj.exercises.all()
        return ", ".join([exercise.name for exercise in exercises])

    def get_exercises(self, obj):
        # Get all related exercises
        exercises = obj.exercises.all()

        # Create a link to each exercise's change page in the admin
        return format_html_join(
            ", ",
            '<a href="{}">{}</a>',
            (
                (
                    # reverse(
                    #     "admin:common_trainingexercise_change", args=[exercise.pk]
                    # ),
                    reverse(
                        "admin:%s_%s_change"
                        % (exercise._meta.app_label, exercise._meta.model_name),
                        args=[exercise.pk],
                    ),
                    str(exercise),
                )
                for exercise in exercises
            ),
        )

    get_exercises.short_description = "Exercises"
    exercise_list.short_description = "Exercise Names"
    exercise_count.short_description = "Number of Exercises"
