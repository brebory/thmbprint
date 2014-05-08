from django.shortcuts import render_to_response, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from profiles.models import UserProfile


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
    """
    logout logs out the current user and ends the session, returning the user to the home page
    @rtype : HttpResponseRedirect
    @param request: HttpRequest object with request details
    @return: HttpResponseRedirect to 'home' view
    """
    auth_logout(request)
    return redirect('home')


def register(request):
    """
    register provides a view for users to sign up for a new account.
    @rtype : HttpResponse
    @param request: HttpRequest object with request details
    @return: HttpResponseRedirect to 'dashboard' view
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Create the UserProfile for the new user
            UserProfile.objects.create(user=new_user)

            return redirect('/user/dashboard/')
    else:
        form = UserCreationForm()

    context = { 'form': form }
    context.update(csrf(request))
    return render_to_response(
        "registration/register.jade",
        context
    )


def about(request):
    return HttpResponse("Under Construction")


def support(request):
    return HttpResponse("Under Construction")


def explore(request):
    return HttpResponse("Under Construction")


def resources(request):
    return HttpResponse("Under Construction")

