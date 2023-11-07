from django.db import models
from common.models.common import UserTimeStamp


class ClimbingAssessments(UserTimeStamp):
    pass


class PowerEnduranceTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="power_endurance_tests",
        on_delete=models.CASCADE,
        null=True,
    )
    seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        seconds_str = (
            f"{self.seconds} seconds"
            if self.seconds is not None
            else "No Time Recorded"
        )
        return f"{assessment_str}, {seconds_str}"


class MaxPullupsTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="max_pullups_tests",
        on_delete=models.CASCADE,
        null=True,
    )
    reps = models.IntegerField(null=True, blank=True)

    def __str__(self):
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        reps_str = f"{self.reps} reps" if self.reps is not None else "No Reps Recorded"
        return f"{assessment_str}, {reps_str}"


class MaxLockoffTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="max_lockoff_tests",
        on_delete=models.CASCADE,
        null=True,
    )
    seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        seconds_str = (
            f"{self.seconds} seconds"
            if self.seconds is not None
            else "No Time Recorded"
        )
        return f"{assessment_str}, {seconds_str}"


class FingerStrengthTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="finger_strength_tests",
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
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        total_load_str = (
            f"{self.total_load} total_load"
            if self.total_load is not None
            else "No Total Load Recorded"
        )
        percentage_bodyweight_str = (
            f"{self.percentage_bodyweight} percentage_bodyweight"
            if self.percentage_bodyweight is not None
            else "No Percentage Bodyweight Recorded"
        )
        return f"{assessment_str}, {total_load_str}, {percentage_bodyweight_str}"


class OAFingerStrengthTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="oa_finger_strength_tests",
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
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        left_str = f"{self.left} left" if self.left is not None else "No Left Recorded"
        right_str = (
            f"{self.right} right"
            if self.right is not None
            else "No Percentage Bodyweight Recorded"
        )
        left_percentage_str = (
            f"{self.left_percentage} left_percentage"
            if self.left_percentage is not None
            else "No Percentage Bodyweight Recorded"
        )
        right_percentage_str = (
            f"{self.right_percentage} right_percentage"
            if self.right_percentage is not None
            else "No Percentage Bodyweight Recorded"
        )
        return f"{assessment_str}, {left_str}, {right_str}, {left_percentage_str}, {right_percentage_str}"


class OAPinchTest(UserTimeStamp):
    assessment = models.ForeignKey(
        ClimbingAssessments,
        related_name="oa_pinch_tests",
        on_delete=models.CASCADE,
        null=True,
    )
    left = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    right = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        assessment_str = (
            f"Assessment ID: {self.assessment.id}"
            if self.assessment
            else "No Assessment"
        )
        left_str = f"{self.left} left" if self.left is not None else "No Left Recorded"
        right_str = (
            f"{self.right} right"
            if self.right is not None
            else "No Percentage Bodyweight Recorded"
        )
        return f"{assessment_str}, {left_str}, {right_str}"
