from django.urls import path, include
from .views import (
    getRoutes,
    handle_otw_plan,
    handle_otw_input,
    handle_gym_input,
    handle_gym_plan,
    handle_prehab_input,
    handle_prehab_plan,
    handle_health_markers,
    handle_health_markers_input,
)


urlpatterns = [
    path("", getRoutes, name="routes"),
    path("plans/otw/create/", handle_otw_input, name="create-otw-plan"),
    path("plans/otw/<int:pk>/", handle_otw_plan, name="otw-plan"),
    path("plans/gym/create/", handle_gym_input, name="create-gym-plan"),
    path("plans/gym/<int:pk>/", handle_gym_plan, name="gym-plan"),
    path("plans/prehab/create/", handle_prehab_input, name="create-prehab-plan"),
    path("plans/prehab/<int:pk>/", handle_prehab_plan, name="prehab-plan"),
    path(
        "assessments/health-markers/create/",
        handle_health_markers_input,
        name="create-health-marker-test",
    ),
    path(
        "assessments/health-markers/<int:pk>/",
        handle_health_markers,
        name="health-marker-test",
    )
    # path(
    #     "plans/<int:otw_plan_id>/exercises/",
    #     get_otw_exercises,
    #     name="get-otw-exercises",
    # ),
]
