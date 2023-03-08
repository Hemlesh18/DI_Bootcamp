from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:pk>/', views.family_view, name='family'),
    path('animal/<int:pk>/', views.animal_view, name='animal'),
]
