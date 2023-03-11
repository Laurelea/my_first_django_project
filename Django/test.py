from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1>This is views!</h1>')

# Create your views here.
