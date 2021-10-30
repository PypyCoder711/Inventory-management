from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return HttpRequest('<h1>Blog home</h1>')





# Create your views here.
