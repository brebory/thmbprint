from django.shortcuts import render_to_response, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from profiles.models import UserProfile, Project
from forms import LoginForm

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

def userlogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('home')
    else:
        form = LoginForm()
        
    context = { 'form': form }
    context.update(csrf(request))
    return render_to_response(
        "userlogin.jade",
         context
    )


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

            return redirect('/userlogin/')
    else:
        form = UserCreationForm()

    context = { 'form': form }
    context.update(csrf(request))
    return render_to_response(
        "registration/register.jade",
        context
    )


def about(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('about.jade', c, RequestContext(request))


def explore(request):
    """
    The explore view retrieves all projects from the database and displays them
    in descending order by date. It is used by users to explore the site and
    check out other user's projects and profiles.
    @rtype : HttpResponse
    @param request: HttpRequest object with request details
    @return: HttpResponse with the rendered explore.jade template
    """

    projects = Project.objects.all().order_by('-created_at')
    c = { 'projects': projects }
    c.update(csrf(request))
    return render_to_response('explore.jade', c, RequestContext(request))
    return HttpResponse("Under Construction")


def resources(request):
    return HttpResponse("Under Construction")

