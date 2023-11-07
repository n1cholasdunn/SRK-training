from django.urls import path


from .views import (
    getRoutes,
    # handle_otw_plan,
    # handle_otw_input,
    # handle_gym_input,
    # handle_gym_plan,
    # handle_prehab_input,
    # handle_prehab_plan,
)


urlpatterns = [
    path("", getRoutes, name="routes"),
    # path("plans/otw/create/", handle_otw_input, name="create-otw-plan"),
    # path("plans/otw/<int:pk>/", handle_otw_plan, name="otw-plan"),
    # path("plans/gym/create/", handle_gym_input, name="create-gym-plan"),
    # path("plans/gym/<int:pk>/", handle_gym_plan, name="gym-plan"),
    # path("plans/prehab/create/", handle_prehab_input, name="create-prehab-plan"),
    # path("plans/prehab/<int:pk>/", handle_prehab_plan, name="prehab-plan"),
    # Health Markers
    # path(
    #     "assessments/health-markers/create/",
    #     handle_health_markers_input,
    #     name="create-health-marker-test",
    # ),
    # path(
    #     "tests/health-markers/<int:pk>/",
    #     handle_health_markers_tests,
    #     name="get-health-marker-test",
    # ),
    # path(
    #     "tests/health-markers/update/<int:pk>/",
    #     handle_health_markers_tests,
    #     name="update-health-marker-test",
    # ),
    # path(
    #     "tests/health-markers/delete/<int:pk>/",
    #     handle_health_markers_tests,
    #     name="delete-health-marker-test",
    # ),
    # # measurements
    # path(
    #     "assessments/measurements/create/",
    #     handle_measurements_input,
    #     name="create-measurements-test",
    # ),
    # path(
    #     "tests/measurements/<int:pk>/",
    #     handle_measurements_tests,
    #     name="get-measurements-test",
    # ),
    # path(
    #     "tests/measurements/update/<int:pk>/",
    #     handle_measurements_tests,
    #     name="update-measurements-test",
    # ),
    # path(
    #     "tests/measurements/delete/<int:pk>/",
    #     handle_measurements_tests,
    #     name="delete-measurements-test",
    # ),
    # # Overhead Squats
    # path(
    #     "assessments/overhead-squats/create/",
    #     handle_overhead_squat_input,
    #     name="create-overhead-squats-test",
    # ),
    # path(
    #     "tests/overhead-squats/<int:pk>/",
    #     handle_overhead_squat_tests,
    #     name="get-overhead-squats-test",
    # ),
    # path(
    #     "tests/overhead-squats/update/<int:pk>/",
    #     handle_overhead_squat_tests,
    #     name="update-overhead-squats-test",
    # ),
    # path(
    #     "tests/overhead-squats/delete/<int:pk>/",
    #     handle_overhead_squat_tests,
    #     name="delete-overhead-squats-test",
    # ),
    # # YMCA Step Test
    # path(
    #     "assessments/ymca-step/create/",
    #     handle_ymca_step_input,
    #     name="create-ymca-step-test",
    # ),
    # path(
    #     "tests/ymca-step/<int:pk>/",
    #     handle_ymca_step_tests,
    #     name="get-ymca-step-test",
    # ),
    # path(
    #     "tests/ymca-step/update/<int:pk>/",
    #     handle_ymca_step_tests,
    #     name="update-ymca-step-test",
    # ),
    # path(
    #     "tests/ymca-step/delete/<int:pk>/",
    #     handle_ymca_step_tests,
    #     name="delete-ymca-step-test",
    # ),
    # # Sit & Reach
    # path(
    #     "assessments/sit-reach/create/",
    #     handle_sit_reach_input,
    #     name="create-sit-reach-test",
    # ),
    # path(
    #     "tests/sit-reach/<int:pk>/",
    #     handle_sit_reach_tests,
    #     name="get-sit-reach-test",
    # ),
    # path(
    #     "tests/sit-reach/update/<int:pk>/",
    #     handle_sit_reach_tests,
    #     name="update-sit-reach-test",
    # ),
    # path(
    #     "tests/sit-reach/delete/<int:pk>/",
    #     handle_sit_reach_tests,
    #     name="delete-sit-reach-test",
    # ),
    # # Pushups
    # path(
    #     "assessments/pushups/create/",
    #     handle_pushup_input,
    #     name="create-pushups-test",
    # ),
    # path(
    #     "assessments/pushups/<int:pk>/",
    #     handle_pushup_assessments,
    #     name="get-pushups-assessments",
    # ),
    # path(
    #     "assessments/pushups/<int:pk>/delete",
    #     handle_pushup_assessments,
    #     name="delete-all-pushups-tests",
    # ),
    # path(
    #     "tests/pushups/<int:pk>/",
    #     handle_pushup_tests,
    #     name="get-pushups-test",
    # ),
    # path(
    #     "tests/pushups/update/<int:pk>/",
    #     handle_pushup_tests,
    #     name="update-pushups-test",
    # ),
    # path(
    #     "tests/pushups/delete/<int:pk>/",
    #     handle_pushup_tests,
    #     name="delete-pushups-test",
    # ),
    # # Davies test
    # path(
    #     "assessments/davies/create/",
    #     handle_davies_input,
    #     name="create-davies-test",
    # ),
    # path(
    #     "tests/davies/<int:pk>/",
    #     handle_davies_tests,
    #     name="get-davies-test",
    # ),
    # path(
    #     "tests/davies/update/<int:pk>/",
    #     handle_davies_tests,
    #     name="update-davies-test",
    # ),
    # path(
    #     "tests/davies/delete/<int:pk>/",
    #     handle_davies_tests,
    #     name="delete-davies-test",
    # ),
    # # Core Test
    # path(
    #     "assessments/core/create/",
    #     handle_core_input,
    #     name="create-core-test",
    # ),
    # path(
    #     "tests/core/<int:pk>/",
    #     handle_core_tests,
    #     name="get-core-test",
    # ),
    # path(
    #     "tests/core/update/<int:pk>/",
    #     handle_core_tests,
    #     name="update-core-test",
    # ),
    # path(
    #     "tests/core/delete/<int:pk>/",
    #     handle_core_tests,
    #     name="delete-core-test",
    # ),
    # # Shark Skills
    # path(
    #     "assessments/shark-skills/create/",
    #     handle_shark_skills_input,
    #     name="create-shark-skills-test",
    # ),
    # path(
    #     "tests/shark-skills/<int:pk>/",
    #     handle_shark_skills_tests,
    #     name="get-shark-skills-test",
    # ),
    # path(
    #     "tests/shark-skills/update/<int:pk>/",
    #     handle_shark_skills_tests,
    #     name="update-shark-skills-test",
    # ),
    # path(
    #     "tests/shark-skills/delete/<int:pk>/",
    #     handle_shark_skills_tests,
    #     name="delete-shark-skills-test",
    # ),
]
