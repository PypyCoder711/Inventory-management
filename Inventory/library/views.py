from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request,'library/base.html')





# Create your views here.
