from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from profiles.models import UserProfile, StudentUser, MentorUser
from profiles.models import Project, ProjectItem
from profiles.models import ProjectItemImage, ProjectItemFile, Recommendation
from profiles.forms import ProjectForm
import urllib
import urllib2

@login_required
def dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user.pk)
    projects = Project.objects.filter(profile=profile)
    c = { "profile": profile, "projects": projects }
    return render(request, 'dashboard.jade', c)

def list_user_projects(request):
    profile = get_object_or_404(UserProfile, user=request.user.pk)
    projects = profile.project_set
    c = {"profile": profile, "projects": projects}
    return render(request, 'list_projects.jade', c)

@login_required
def create_project(request):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user.pk)
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit = False)
            project.profile = profile
            project.save()
            return redirect('profiles:dashboard')
    else:
        form = ProjectForm()
    c = { "form": form }
    return render(request, "create_project.jade", c)

def project_detail(request, project_id):
    profile = get_object_or_404(UserProfile, user=request.user.pk)
    project = get_object_or_404(Project, pk=project_id)
    c = { "profile": profile,
          "project": project }
    return render(request, "project_detail.jade", c)

@login_required
def edit_project(request, project_id):
    profile = get_object_or_404(UserProfile, user=request.user.pk)
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        formset = ProjectItemFormset(request.POST, instance=project)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(
                    'profiles:project_detail',
                    project_id=project_id
            )
    else:
        form = ProjectForm(instance=project)
        formset = ProjectItemFormset(instance=project)
    c = {
            "form": form,
            "formset": formset,
            "project": project,
            "profile": profile
    }
    c.update(csrf(request))
    return render(request, "edit_project.jade", c)

def get_badges(user):
    """ 
    Returns the user's mozilla open badges
    """
    badges = []
    url = "http://beta.openbadges.org/displayer/convert/email"
    values = { 'email': user.email }
    data = urllib.urlencode(values)
    result = urllib2.urlopen(url, data)
    if result.status == "okay":
        url = "http://beta.openbadges.org/displayer/%s/groups.json" % result.userId
        result = urllib2.urlopen(url)
        if result.groups:
            for group in result.groups:
                url = "http://beta.openbadges.org/displayer/%s/groups/:wq"

    else:
        badges = [{ "error": "couldn't open user's badge backpack" }]



