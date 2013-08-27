from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
    return render_to_response('home.jade')

def login(request):
    return HttpResponse("Under Construction")

def register(request):
    return HttpResponse("Under Construction")

def about(request):
    return HttpResponse("Under Construction")

def support(request):
    return HttpResponse("Under Construction")
