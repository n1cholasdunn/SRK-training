from django.urls import path
from react_forms.views import (
    handle_availability,
    handle_equipment,
    handle_general_client_info,
    handle_max_pullups_test,
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
    # path(
    #     "assessments/climbing/testing/create/",
    #     handle_power_endurance_test,
    #     name="handle-power-endurance-test",
    # ),
    # path(
    #     "assessments/climbing/testing/create/",
    #     handle_max_pullups_test,
    #     name="handle-max-pullup-test",
    # ),
    path(
        "assessments/climbing/testing/create/",
        handle_max_lockoff_test,
        name="handle-max-lockoff-test",
    ),
]
