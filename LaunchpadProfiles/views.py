from django.shortcuts import render_to_response, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('home.jade', c, RequestContext(request))

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
    return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('home')

def register(request):
    return HttpResponse("Under Construction")

def about(request):
    return HttpResponse("Under Construction")

def support(request):
    return HttpResponse("Under Construction")
