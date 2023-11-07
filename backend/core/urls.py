from django.contrib import admin
from django.urls import path, include
from core.views import get_user_info

urlpatterns = [
    path("info/", get_user_info, name="user-info"),
]
