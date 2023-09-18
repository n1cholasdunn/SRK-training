from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OTWTrainingPlan
from .serializers import OTWTrainingPlanSerializer
from django.http import response
from .utils import (
    get_otw_plans_list,
    create_otw_plan,
    get_otw_plan_detail,
    update_otw_plan,
    delete_otw_plan,
)


# Create your views here.
@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            # TODO add in userId after Oauth is added
            "Endpoint": "/plans/otw/",
            "method": "GET",
            "body": None,
            "description": "Returns OTW training plans in descending order",
        },
        {
            "Endpoint": "/plans/otw/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new OTW training plan",
        },
        {
            "Endpoint": "/plans/otw/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing OTW training plan",
        },
        {
            "Endpoint": "/plans/otw/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes OTW existing training plan",
        },
        {
            "Endpoint": "/plans/gym/",
            "method": "GET",
            "body": None,
            "description": "Returns gym training plans in descending order",
        },
        {
            "Endpoint": "/plans/gym/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new gym training plan",
        },
        {
            "Endpoint": "/plans/gym/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing gym training plan",
        },
        {
            "Endpoint": "/plans/gym/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes gym existing training plan",
        },
        {
            "Endpoint": "/plans/prehab/",
            "method": "GET",
            "body": None,
            "description": "Returns prehab training plans in descending order",
        },
        {
            "Endpoint": "/plans/prehab/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "creates a new prehab training plan",
        },
        {
            "Endpoint": "/plans/prehab/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "updates existing prehab training plan",
        },
        {
            "Endpoint": "/plans/prehab/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "deletes prehab existing training plan",
        },
    ]
    return Response(routes)


@api_view(["GET", "POST"])
def get_otw_plans(request):
    if request.method == "GET":
        return get_otw_plans_list(request)

    if request.method == "POST":
        return create_otw_plan(request)


@api_view(["GET", "PUT", "DELETE"])
def get_otw_plan(request, pk):
    if request.method == "GET":
        return get_otw_plan_detail(request, pk)

    if request.method == "PUT":
        return update_otw_plan(request, pk)

    if request.method == "DELETE":
        return delete_otw_plan(request, pk)
