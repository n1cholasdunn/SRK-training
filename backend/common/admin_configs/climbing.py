from django.contrib import admin
from common.models.climbing_models import (
    PowerEnduranceTest,
    MaxLockoffTest,
    MaxPullupsTest,
    FingerStrengthTest,
    OAFingerStrengthTest,
    OAPinchTest,
)


@admin.register(PowerEnduranceTest)
class PowerEnduranceTestAdmin(admin.ModelAdmin):
    pass


@admin.register(MaxLockoffTest)
class MaxLockoffTestAdmin(admin.ModelAdmin):
    pass


@admin.register(MaxPullupsTest)
class MaxPullupsTestAdmin(admin.ModelAdmin):
    pass


@admin.register(FingerStrengthTest)
class FingerStrengthTestAdmin(admin.ModelAdmin):
    pass


@admin.register(OAFingerStrengthTest)
class OAFingerStrengthTestAdmin(admin.ModelAdmin):
    pass


@admin.register(OAPinchTest)
class OAPinchTestAdmin(admin.ModelAdmin):
    pass
