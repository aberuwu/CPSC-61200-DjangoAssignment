from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    helloWorld = {'Message': "Hello World"}
    return JsonResponse(helloWorld)
