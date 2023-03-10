from django.urls import path
from . import views

urlpatterns = [
    path('phonenumber/', views.by_phone_number, name='by_phone_number'),
    path('name/', views.by_name, name='by_name'),
]
