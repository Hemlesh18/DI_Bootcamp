from django.shortcuts import render
from .models import person
# Create your views here.
def population_database():
    for person_data in people:
        person.objects.create(**person_data)
population_database()

def people_list(request):
    people= person.objects.order_by('age')
    return render(request, 'people_list.html', {'people': people})
def person_detail(request,id):
    person = person.objects.get(id=id)
    return render(request, 'person_detail.html', {'person': person})

def people_list(request):
    people = Person.objects.order_by('age')
    return render(request, 'people_list.html', {'people': people})

def person_detail(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'person_detail.html', {'person': person})