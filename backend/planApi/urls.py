from django.urls import path, include
from .views import get_otw_plans, getRoutes, get_otw_plan


urlpatterns = [
    path("", getRoutes, name="routes"),
    path("plans/otw/", get_otw_plans, name="otw-plans"),
    path("plans/otw/<int:pk>/", get_otw_plan, name="otw-plan"),
    # path("/plans/gym/", get_gym_plans, name="otw-plans"),
    # path("plans/gym/<int:pk>/", get_gym_plan, name="gym-plan"),
]
