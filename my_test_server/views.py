from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def test_return(request):
    return HttpResponse("hello world, how are you?")