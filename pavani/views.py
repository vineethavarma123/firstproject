from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('<h1><marquee>This is our first FBV</h1></marquee>')
