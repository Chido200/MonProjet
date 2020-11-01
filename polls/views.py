from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('tu es bien pour démarré')    

# Create your views here.
