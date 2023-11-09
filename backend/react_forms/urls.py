from venv import create
from django.urls import path
from react_forms.utils.climbing.create_multiple_tests import (
    create_multiple_tests,
)
from react_forms.views import (
    handle_availability,
    handle_equipment,
    handle_finger_strength_test,
    handle_general_client_info,
    handle_max_pullups_test,
    handle_oa_finger_strength_test,
    handle_oa_pinch_strength_test,
    handle_program,
    handle_power_endurance_test,
    handle_max_lockoff_test,
)

urlpatterns = [
    path(
        "client/availability",
        handle_availability,
        name="handle-availability",
    ),
    # TODO make path dynamic for username or something
    path(
        "client/info/",
        handle_general_client_info,
        name="handle-general-client-info",
    ),
    path(
        "client/equipment/",
        handle_equipment,
        name="handle-equipment",
    ),
    path(
        "client/program/",
        handle_program,
        name="handle-program",
    ),
    path(
        "assessments/climbing/power-endurance/",
        handle_power_endurance_test,
        name="handle-power-endurance-test",
    ),
    path(
        "assessments/climbing/max-pullup/",
        handle_max_pullups_test,
        name="handle-max-pullup-test",
    ),
    path(
        "assessments/climbing/max-lockoff/",
        handle_max_lockoff_test,
        name="handle-max-lockoff-test",
    ),
    path(
        "assessments/climbing/finger-strength/",
        handle_finger_strength_test,
        name="handle-finger-strength-test",
    ),
    path(
        "assessments/climbing/oa-finger-strength/",
        handle_oa_finger_strength_test,
        name="handle-oa-finger-strength-test",
    ),
    path(
        "assessments/climbing/oa-pinch-strength/",
        handle_oa_pinch_strength_test,
        name="handle-oa-pinch-test",
    ),
    path(
        "assessments/climbing/all/",
        create_multiple_tests,
        name="handle-oa-pinch-test",
    ),
]
