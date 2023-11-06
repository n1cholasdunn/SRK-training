from django.urls import path
from react_forms.views import handle_availability, handle_general_client_info

urlpatterns = [
    path(
        "client/availability",
        handle_availability,
        name="handle-availability",
    ),
    # TODO make path dynamic for username or something
    path(
        "client/info",
        handle_general_client_info,
        name="handle-general-client-info",
    ),
]
