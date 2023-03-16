from django.shortcuts import render
from django.http import HttpResponse
# from .models import people

persons =[
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people_list(request):
    sorted_people = sorted(persons, key=lambda p: p['age'])
    return render(request, 'people_list.html', {'people': sorted_people})

def person_detail(request, id):
    person = next((p for p in persons if p['id'] == id), None)
    print(person)
    return render(request, 'person_detail.html', {'person': person})
