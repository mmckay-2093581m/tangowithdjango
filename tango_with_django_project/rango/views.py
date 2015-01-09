from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    pageHtml = "Rango says hey there world!" +\
    "<br/><a href='/rango/about/'>About</a>"

    return HttpResponse(pageHtml)

def about(request):
    pageHtml = "Rango says here is the about page." +\
   "<br/><a href='/rango/'>Index</a>"

    return HttpResponse(pageHtml)