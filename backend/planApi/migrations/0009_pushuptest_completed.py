# Generated by Django 4.2.2 on 2023-10-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planApi', '0008_rename_measurement_sitreachtest_first_measurement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushuptest',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
