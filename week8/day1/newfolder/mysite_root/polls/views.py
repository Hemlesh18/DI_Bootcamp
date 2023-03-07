# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from pkgutil import get_data
from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render

def hello(request):
    context = get_data(...) # fetch the data you need
    return render(request, "myapp/template/hello.html", context)

def hello(request):
    return render(request, "myapp/template/hello.html", {})
def hello(request):
    context = get_data('..vggghvvghvghvgvgvghghgvgv.') # fetch the data you need
    return render(request, "myapp/template/hello.html", context)

def month_archive(self, season, month):
    context = {
        'season':season,
        'month':month
    }
    return render(request, 'index.html', context)