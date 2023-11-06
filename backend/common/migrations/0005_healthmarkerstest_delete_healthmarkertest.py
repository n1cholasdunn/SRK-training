# Generated by Django 4.2.2 on 2023-10-02 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0004_coreassessments_daviesassessments_dayavailability_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthMarkersTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marker", models.CharField(max_length=25)),
                (
                    "weight",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "bmi",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "waist_hip_ratio",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "resting_hr",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "blood_pressure",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "vo2_max",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=2, null=True
                    ),
                ),
                (
                    "assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tests",
                        to="common.healthmarkersassessments",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="HealthMarkerTest",
        ),
    ]
