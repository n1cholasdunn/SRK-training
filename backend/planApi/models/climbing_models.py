from django.db import models
from core.models import User


class BaseAssessment(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PowerEnduranceAssessments(BaseAssessment):
    pass


class PowerEnduranceTest(models.Model):
    assessment = models.ForeignKey(
        "PowerEnduranceAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class MaxPullupsAssessments(BaseAssessment):
    pass


class MaxPullupsTest(models.Model):
    assessment = models.ForeignKey(
        "MaxPullupsAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class MaxLockoffAssessments(BaseAssessment):
    pass


class MaxLockoffTest(models.Model):
    assessment = models.ForeignKey(
        "MaxLockoffAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class FingerStrengthAssessments(BaseAssessment):
    pass


class FingerStrengthTest(models.Model):
    assessment = models.ForeignKey(
        "FingerStrengthAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class OAFingerStrengthAssessments(BaseAssessment):
    pass


class OAFingerStrengthTest(models.Model):
    assessment = models.ForeignKey(
        "OAFingerStrengthAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class OAPinchAssessments(BaseAssessment):
    pass


class OAPinchTest(models.Model):
    assessment = models.ForeignKey(
        "OAPinchAssessment", related_name="tests", on_delete=models.CASCADE
    )
    test = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"
