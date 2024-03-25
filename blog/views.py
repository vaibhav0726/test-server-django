from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the blogs index.")

def blog(request):
    return HttpResponse("Hello, vaibhav. You're at the blogs response.")