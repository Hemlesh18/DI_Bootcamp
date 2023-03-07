from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people, name='people'),
    path('people/<int:id>/', views.person, name='person'),
]
