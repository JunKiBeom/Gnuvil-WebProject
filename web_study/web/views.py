from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Index.")
    return  render(request, 'gnuvil.html')

def hello(request):
    return render(request, 'hello.html')