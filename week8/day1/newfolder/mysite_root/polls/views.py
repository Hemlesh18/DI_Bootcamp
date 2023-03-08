# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response


from pkgutil import get_data
# # from django.shortcuts import render
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render

def hello(request):
     # fetch the data you need
    return render(request, "myapp/template/hello.html")

# from django.http import HttpResponse
# from django.template import loader

# def index(request):
#     template = loader.get_template('polls/index.html')
#     context = get_data('..vggghvvghvghvgvgvghghgvgv.')
#     return HttpResponse(template.render(context, request))
from django.shortcuts import render

def index(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/homepage.html', context)