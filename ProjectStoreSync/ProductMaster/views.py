from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is index page')

def other(request):
    return HttpResponse('This is other page')
