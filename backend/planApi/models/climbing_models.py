from django.db import models
from core.models import User


class BaseAssessment(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PowerEnduranceAssessment(BaseAssessment):
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)
    test11 = models.CharField(max_length=5, null=True, blank=True)


class MaxPullupsAssessment(BaseAssessment):
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)
    test11 = models.CharField(max_length=5, null=True, blank=True)


class MaxLockoffAssessment(BaseAssessment):
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)
    test11 = models.CharField(max_length=5, null=True, blank=True)


class FingerStrengthAssessment(BaseAssessment):
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)


class OAFingerStrengthAssessment(BaseAssessment):
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)


class OAPinchAssessment(BaseAssessment):
    # TODO find best method for if inputting 1 test at a time over time. all tests prenamed like below or seperate model that is connected but presents problem of limiting it
    pre_training_test = models.CharField(max_length=5, null=True, blank=True)
    test1 = models.CharField(max_length=5, null=True, blank=True)
    test2 = models.CharField(max_length=5, null=True, blank=True)
    test3 = models.CharField(max_length=5, null=True, blank=True)
    test4 = models.CharField(max_length=5, null=True, blank=True)
    test5 = models.CharField(max_length=5, null=True, blank=True)
    test6 = models.CharField(max_length=5, null=True, blank=True)
    test7 = models.CharField(max_length=5, null=True, blank=True)
    test8 = models.CharField(max_length=5, null=True, blank=True)
    test9 = models.CharField(max_length=5, null=True, blank=True)
    test10 = models.CharField(max_length=5, null=True, blank=True)


# class OAPinchTests(models.Model):
#     assessment = models.ForeignKey(
#         "OAPinchAssessment", related_name="tests", on_delete=models.CASCADE
#     )
#     weight = models.CharField(max_length=10, null=True, blank=True)
#     bmi = models.CharField(max_length=6, null=True, blank=True)
#     waist_hip_ratio = models.CharField(max_length=6, null=True, blank=True)
#     resting_hr = models.CharField(max_length=6, null=True, blank=True)
#     blood_pressure = models.CharField(max_length=6, null=True, blank=True)
#     vo2_max = models.CharField(max_length=6, null=True, blank=True)
