# Generated by Django 4.2.2 on 2023-09-28 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planApi', '0003_prehabtrainingexercise_gymtrainingexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DaviesAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DayAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('am', models.CharField(blank=True, max_length=25, null=True)),
                ('pm', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FingerStrengthAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthMarkersAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaxLockoffAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaxPullupsAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeasurementsAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OAFingerStrengthAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OAPinchAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OverheadSquatAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PowerEnduranceAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PushUpAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SharkSkillsAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SharkSkillsSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('deduction_tally', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('total_deducted', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('final_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SitReachAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YMCAStepAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YMCAStepTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recovery_hr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rating', models.CharField(blank=True, max_length=25, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.ymcastepassessments')),
            ],
        ),
        migrations.CreateModel(
            name='SitReachTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.sitreachassessments')),
            ],
        ),
        migrations.CreateModel(
            name='SharkSkillsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.sharkskillsassessments')),
                ('first_left', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_lefts', to='planApi.sharkskillsside')),
                ('first_right', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_rights', to='planApi.sharkskillsside')),
                ('practice_left', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='practice_lefts', to='planApi.sharkskillsside')),
                ('practice_right', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='practice_rights', to='planApi.sharkskillsside')),
                ('second_left', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_lefts', to='planApi.sharkskillsside')),
                ('second_right', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_rights', to='planApi.sharkskillsside')),
            ],
        ),
        migrations.CreateModel(
            name='PushUpTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pushups', models.IntegerField(blank=True, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.pushupassessments')),
            ],
        ),
        migrations.CreateModel(
            name='PowerEnduranceTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.powerenduranceassessments')),
            ],
        ),
        migrations.CreateModel(
            name='OverheadSquatTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foot_ankle', models.CharField(blank=True, max_length=250, null=True)),
                ('knee', models.CharField(blank=True, max_length=250, null=True)),
                ('lphc', models.CharField(blank=True, max_length=250, null=True)),
                ('shoulder', models.CharField(blank=True, max_length=250, null=True)),
                ('solutions', models.TextField(blank=True, max_length=750, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.overheadsquatassessments')),
            ],
        ),
        migrations.CreateModel(
            name='OAPinchTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.oapinchassessments')),
            ],
        ),
        migrations.CreateModel(
            name='OAFingerStrengthTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.oafingerstrengthassessments')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('biceps', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('forearms', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lower_abdomen', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hips', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('upper_thigh', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('mid_thigh', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('calves', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.measurementsassessments')),
            ],
        ),
        migrations.CreateModel(
            name='MaxPullupsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.IntegerField(blank=True, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.maxpullupsassessments')),
            ],
        ),
        migrations.CreateModel(
            name='MaxLockoffTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.maxlockoffassessments')),
            ],
        ),
        migrations.CreateModel(
            name='HealthMarkerTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bmi', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('waist_hip_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('resting_hr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('blood_pressure', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vo2_max', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.healthmarkersassessments')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralClientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=75)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('emergency_contact', models.CharField(max_length=255)),
                ('emergency_phone', models.CharField(max_length=255)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
                ('ape_index', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_goals', models.CharField(max_length=255)),
                ('health_concerns', models.CharField(blank=True, max_length=255, null=True)),
                ('parq_complete', models.BooleanField(default=False)),
                ('liability_waiver', models.BooleanField(default=False)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FingerStrengthTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.fingerstrengthassessments')),
            ],
        ),
        migrations.CreateModel(
            name='DaviesTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_trial', models.IntegerField(blank=True, null=True)),
                ('second_trial', models.IntegerField(blank=True, null=True)),
                ('third_trial', models.IntegerField(blank=True, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.daviesassessments')),
            ],
        ),
        migrations.CreateModel(
            name='CoreTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_trial', models.CharField(blank=True, max_length=6, null=True)),
                ('second_trial', models.CharField(blank=True, max_length=6, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='planApi.coreassessments')),
            ],
        ),
        migrations.CreateModel(
            name='ClientProgramInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('program_type', models.CharField(max_length=30)),
                ('training_style', models.CharField(max_length=30)),
                ('payment_rate', models.CharField(max_length=25)),
                ('program_start', models.CharField(blank=True, max_length=25, null=True)),
                ('outdoor_max', models.CharField(blank=True, max_length=5, null=True)),
                ('outdoor_flash', models.CharField(blank=True, max_length=5, null=True)),
                ('indoor_max', models.CharField(blank=True, max_length=5, null=True)),
                ('indoor_flash', models.CharField(blank=True, max_length=5, null=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_equipment', to='planApi.equipment')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('friday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_availability', to='planApi.dayavailability')),
                ('monday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_availability', to='planApi.dayavailability')),
                ('saturday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_availability', to='planApi.dayavailability')),
                ('sunday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_availability', to='planApi.dayavailability')),
                ('thursday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_availability', to='planApi.dayavailability')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tuesday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_availability', to='planApi.dayavailability')),
                ('wednesday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_availability', to='planApi.dayavailability')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
