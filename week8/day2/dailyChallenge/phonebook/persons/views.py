from django.shortcuts import render
from .models import Person

def by_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            person = Person.objects.get(phone_number=phone_number)
            return render(request, 'persons/person_info.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'persons/person_info.html', {'error': 'No person found with this phone number.'})
    return render(request, 'persons/search.html', {'title': 'Search by phone number'})

def by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            person = Person.objects.get(name=name)
            return render(request, 'persons/person_info.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'persons/person_info.html', {'error': 'No person found with this name.'})
    return render(request, 'persons/search.html', {'title': 'Search by name'})


