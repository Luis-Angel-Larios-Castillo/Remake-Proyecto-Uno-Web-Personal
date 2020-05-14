from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<H1>Mi web personal</H1><H2>Portada</H2>")