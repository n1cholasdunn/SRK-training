# Generated by Django 4.2.2 on 2023-11-06 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planApi', '0012_rename_left_fingerstrengthtest_percentage_bodyweight_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fingerstrengthtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='maxlockofftest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='maxpullupstest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='oafingerstrengthtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='oapinchtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='powerendurancetest',
            name='test',
        ),
    ]
