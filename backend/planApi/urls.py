from django.urls import path, include
from .views import (
    get_otw_plans,
    getRoutes,
    get_otw_plan,
    input_otw_plan_view,
    get_otw_exercises,
)


urlpatterns = [
    path("", getRoutes, name="routes"),
    path("plans/otw/", get_otw_plans, name="otw-plans"),
    path("plans/otw/<int:pk>/", get_otw_plan, name="otw-plan"),
    path("input-otw-plan/", input_otw_plan_view, name="input-otw-plan"),
    path(
        "plans/<int:otw_plan_id>/exercises/",
        get_otw_exercises,
        name="get-otw-exercises",
    ),
    # path("/plans/gym/", get_gym_plans, name="otw-plans"),
    # path("plans/gym/<int:pk>/", get_gym_plan, name="gym-plan"),
]
