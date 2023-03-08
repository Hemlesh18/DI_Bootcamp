from django.shortcuts import render
import json

def family_view(request, pk):
    with open('animal&people.json') as f:
        data = json.load(f)
    animals = [a for a in data['animals&people'] if a['family'] == pk]
    context = {'animals&people': animals}
    return render(request, 'info/family.html', context)

def animal_view(request, pk):
    with open('animal&people.json') as f:
        data = json.load(f)
    animal = next((a for a in data['animals&people'] if a['id'] == pk), None)
    context = {'animal&people': animal}
    return render(request, 'info/animal.html', context)

