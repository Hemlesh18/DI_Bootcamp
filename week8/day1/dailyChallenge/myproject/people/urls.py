from django.urls import path
from .views import people_list,person_detail

urlpatterns=[
    path('people/', people_list, name='people_list'),
    path('people/<int:id>/', person_detail, name='person_detail'),
    
]