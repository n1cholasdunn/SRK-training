from django.db import models
from .common import BaseAssessment


class PowerEnduranceAssessments(BaseAssessment):
    pass


class PowerEnduranceTest(models.Model):
    assessment = models.ForeignKey(
        PowerEnduranceAssessments,
        related_name="tests",
        on_delete=models.CASCADE,
        null=True,
    )
    seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class MaxPullupsAssessments(BaseAssessment):
    pass


class MaxPullupsTest(models.Model):
    assessment = models.ForeignKey(
        MaxPullupsAssessments, related_name="tests", on_delete=models.CASCADE, null=True
    )
    reps = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class MaxLockoffAssessments(BaseAssessment):
    pass


class MaxLockoffTest(models.Model):
    assessment = models.ForeignKey(
        MaxLockoffAssessments, related_name="tests", on_delete=models.CASCADE, null=True
    )
    seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.test}"


class FingerStrengthAssessments(BaseAssessment):
    pass


class FingerStrengthTest(models.Model):
    assessment = models.ForeignKey(
        FingerStrengthAssessments,
        related_name="tests",
        on_delete=models.CASCADE,
        null=True,
    )
    total_load = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    percentage_bodyweight = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return f"{self.test}"


class OAFingerStrengthAssessments(BaseAssessment):
    pass


class OAFingerStrengthTest(models.Model):
    assessment = models.ForeignKey(
        OAFingerStrengthAssessments,
        related_name="tests",
        on_delete=models.CASCADE,
        null=True,
    )
    left = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    right = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    left_percentage = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )
    right_percentage = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return f"{self.test}"


class OAPinchAssessments(BaseAssessment):
    pass


class OAPinchTest(models.Model):
    assessment = models.ForeignKey(
        OAPinchAssessments, related_name="tests", on_delete=models.CASCADE, null=True
    )
    left = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    right = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f"{self.test}"
