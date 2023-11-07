# Generated by Django 4.2.2 on 2023-11-07 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0019_fingerstrengthtest_assessment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimbingAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('trainee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FitnessAssessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('trainee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTWTrainingExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('warmup', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('equipment_used', models.CharField(max_length=100)),
                ('rest', models.CharField(max_length=100)),
                ('sets', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('trainee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='coreassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='daviesassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='fingerstrengthassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='healthmarkersassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='maxlockoffassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='maxpullupsassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='measurementsassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='oafingerstrengthassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='oapinchassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='otwtrainingplan',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='overheadsquatassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='powerenduranceassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='prehabtrainingplan',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='pushupassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='sharkskillsassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='sitreachassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='trainingexercise',
            name='training_plan',
        ),
        migrations.RemoveField(
            model_name='ymcastepassessments',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='gymtrainingexercise',
            name='training_plan',
        ),
        migrations.RemoveField(
            model_name='prehabtrainingexercise',
            name='training_plan',
        ),
        migrations.AddField(
            model_name='coretest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coretest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coretest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daviestest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daviestest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='daviestest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fingerstrengthtest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fingerstrengthtest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fingerstrengthtest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gymtrainingexercise',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gymtrainingexercise',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gymtrainingexercise',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gymtrainingexercise',
            name='warmup',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthmarkerstest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthmarkerstest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='healthmarkerstest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maxlockofftest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maxlockofftest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maxlockofftest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maxpullupstest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maxpullupstest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maxpullupstest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurementstest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurementstest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='measurementstest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oafingerstrengthtest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oafingerstrengthtest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oafingerstrengthtest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oapinchtest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oapinchtest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oapinchtest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overheadsquattest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overheadsquattest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='overheadsquattest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='powerendurancetest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='powerendurancetest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='powerendurancetest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prehabtrainingexercise',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prehabtrainingexercise',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prehabtrainingexercise',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prehabtrainingexercise',
            name='warmup',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pushuptest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pushuptest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pushuptest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sharkskillsside',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sharkskillsside',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharkskillsside',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sharkskillstest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sharkskillstest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharkskillstest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitreachtest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitreachtest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sitreachtest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ymcasteptest',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ymcasteptest',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ymcasteptest',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='GymTrainingPlan',
        ),
        migrations.DeleteModel(
            name='OTWTrainingPlan',
        ),
        migrations.DeleteModel(
            name='PrehabTrainingPlan',
        ),
        migrations.DeleteModel(
            name='TrainingExercise',
        ),
        migrations.AlterField(
            model_name='coretest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='daviestest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='davies_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='fingerstrengthtest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finger_strength_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='healthmarkerstest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_markers_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='maxlockofftest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='max_lockoff_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='maxpullupstest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='max_pullups_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='measurementstest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='oafingerstrengthtest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oa_finger_strength_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='oapinchtest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oa_pinch_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='overheadsquattest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='overhead_squat_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='powerendurancetest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='power_endurance_tests', to='common.climbingassessments'),
        ),
        migrations.AlterField(
            model_name='pushuptest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='push_up_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='sharkskillstest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shark_skills_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='sitreachtest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sit_reach_tests', to='common.fitnessassessments'),
        ),
        migrations.AlterField(
            model_name='ymcasteptest',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ymca_step_tests', to='common.fitnessassessments'),
        ),
        migrations.DeleteModel(
            name='CoreAssessments',
        ),
        migrations.DeleteModel(
            name='DaviesAssessments',
        ),
        migrations.DeleteModel(
            name='FingerStrengthAssessments',
        ),
        migrations.DeleteModel(
            name='HealthMarkersAssessments',
        ),
        migrations.DeleteModel(
            name='MaxLockoffAssessments',
        ),
        migrations.DeleteModel(
            name='MaxPullupsAssessments',
        ),
        migrations.DeleteModel(
            name='MeasurementsAssessments',
        ),
        migrations.DeleteModel(
            name='OAFingerStrengthAssessments',
        ),
        migrations.DeleteModel(
            name='OAPinchAssessments',
        ),
        migrations.DeleteModel(
            name='OverheadSquatAssessments',
        ),
        migrations.DeleteModel(
            name='PowerEnduranceAssessments',
        ),
        migrations.DeleteModel(
            name='PushUpAssessments',
        ),
        migrations.DeleteModel(
            name='SharkSkillsAssessments',
        ),
        migrations.DeleteModel(
            name='SitReachAssessments',
        ),
        migrations.DeleteModel(
            name='YMCAStepAssessments',
        ),
    ]
