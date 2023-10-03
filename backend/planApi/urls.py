from django.urls import path, include
from .views import (
    getRoutes,
    handle_health_markers_tests,
    handle_measurements_assessments,
    handle_measurements_input,
    handle_measurements_tests,
    handle_otw_plan,
    handle_otw_input,
    handle_gym_input,
    handle_gym_plan,
    handle_overhead_squat_assessments,
    handle_overhead_squat_input,
    handle_overhead_squat_tests,
    handle_prehab_input,
    handle_prehab_plan,
    handle_health_markers_assessments,
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
    # health markers
    path(
        "assessments/health-markers/create/",
        handle_health_markers_input,
        name="create-health-marker-test",
    ),
    path(
        "assessments/health-markers/<int:pk>/",
        handle_health_markers_assessments,
        name="get-all-health-marker-tests",
    ),
    path(
        "assessments/health-markers/<int:pk>/delete",
        handle_health_markers_assessments,
        name="delete-all-health-marker-tests",
    ),
    path(
        "tests/health-markers/<int:pk>/",
        handle_health_markers_tests,
        name="get-health-marker-test",
    ),
    path(
        "tests/health-markers/update/<int:pk>/",
        handle_health_markers_tests,
        name="update-health-marker-test",
    ),
    path(
        "tests/health-markers/delete/<int:pk>/",
        handle_health_markers_tests,
        name="delete-health-marker-test",
    ),
    # measurements
    path(
        "assessments/measurements/create/",
        handle_measurements_input,
        name="create-measurements-test",
    ),
    path(
        "assessments/measurements/<int:pk>/",
        handle_measurements_assessments,
        name="get-measurements-assessments",
    ),
    path(
        "assessments/measurements/<int:pk>/delete",
        handle_measurements_assessments,
        name="delete-all-measurements-tests",
    ),
    path(
        "tests/measurements/<int:pk>/",
        handle_measurements_tests,
        name="get-measurements-test",
    ),
    path(
        "tests/measurements/update/<int:pk>/",
        handle_measurements_tests,
        name="update-measurements-test",
    ),
    path(
        "tests/measurements/delete/<int:pk>/",
        handle_measurements_tests,
        name="delete-measurements-test",
    ),
    # overhead squats
    path(
        "assessments/overhead-squats/create/",
        handle_overhead_squat_input,
        name="create-overhead-squats-test",
    ),
    path(
        "assessments/overhead-squats/<int:pk>/",
        handle_overhead_squat_assessments,
        name="get-overhead-squats-assessments",
    ),
    path(
        "assessments/overhead-squats/<int:pk>/delete",
        handle_overhead_squat_assessments,
        name="delete-all-overhead-squats-tests",
    ),
    path(
        "tests/overhead-squats/<int:pk>/",
        handle_overhead_squat_tests,
        name="get-overhead-squats-test",
    ),
    path(
        "tests/overhead-squats/update/<int:pk>/",
        handle_overhead_squat_tests,
        name="update-overhead-squats-test",
    ),
    path(
        "tests/overhead-squats/delete/<int:pk>/",
        handle_overhead_squat_tests,
        name="delete-overhead-squats-test",
    ),
]
