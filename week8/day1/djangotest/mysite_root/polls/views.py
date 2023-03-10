from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. your are tje the polls index.")
    context = {}
    return render(request, "base.html", context)

def about(request):
        context = {}
        return render(request, "about.html", context)

       
