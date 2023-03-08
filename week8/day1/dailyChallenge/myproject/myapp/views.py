from django.shortcuts import render

# Create your views here.

from .models import Person

def people(request):
    people_list = Person.objects.order_by('age')
    return render(request, 'myapp/people.html', {'people_list': people_list})

def person(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'myapp/person.html', {'person': person})
