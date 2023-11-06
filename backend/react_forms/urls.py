from django.urls import path
from react_forms.views import handle_react_availability

urlpatterns = [
    path(
        "client/availability",
        handle_react_availability,
        name="handle-react-availability",
    ),
]
