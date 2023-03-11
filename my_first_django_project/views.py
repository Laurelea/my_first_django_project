from django.shortcuts import render
from django.http import HttpResponse

def view(request):
    return HttpResponse('This is a view!')

def home(request):
    return render (request, 'home.html', {'greeting': 'Hello!'})
# Create your views here.
