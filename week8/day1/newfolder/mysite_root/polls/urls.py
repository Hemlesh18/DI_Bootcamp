from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the routeurlpatterns = [
# urlpatterns = [
#     path('articles/<int:year>/', views.year_archive),
#     path('articles/<str:season>/<int:month>/', views.month_archive),
# ]