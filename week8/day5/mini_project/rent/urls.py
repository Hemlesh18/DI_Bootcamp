from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("fake_data", views.fake_data),
]
