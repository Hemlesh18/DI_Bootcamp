from django.urls import path
from . import views

urlpatterns = [
    path('Person', views.people_list, name='people_list'),
    path('Person/<int:pk>', views.person_detail, name='person_detail'),
]
