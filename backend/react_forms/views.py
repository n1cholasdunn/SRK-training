from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from react_forms.utils.availability import (
    create_availability,
    delete_availability,
    get_availabilities,
    update_availability,
)


# Create your views here.
@api_view(["GET", "PUT", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def handle_react_availability(request, pk):
    if request.method == "GET":
        return get_availabilities(request)
    if request.method == "PUT":
        return update_availability(request, pk)
    if request.method == "POST":
        return create_availability(request)
    if request.method == "DELETE":
        return delete_availability(request, pk)
