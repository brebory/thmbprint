from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from profiles.models import UserProfile, StudentUser, MentorUser
from profiles.models import Project, ProjectItem
from profiles.models import ProjectItemImage, ProjectItemFile, Recommendation
from profiles.forms import ProjectForm

@login_required
def dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user.pk)
    projects = Project.objects.filter(profile=profile)
    c = { "profile": profile, "projects": projects }
    return render(request, 'dashboard.jade', c)

def list_user_projects(request, user_id):
    profile = get_object_or_404(UserProfile, user=user_id)
    projects = profile.project_set
    c = {"profile": profile, "projects": projects}
    return render(request, 'list_projects.jade', c)

def create_project(request, user_id):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=user_id)
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                    profile=profile.pk,
                    name=form.name,
                    description=form.description,
                    start_date=form.start_date,
                    end_date=form.end_date
            )
            project.save()
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

def edit_project(request, user_id, project_id):
    profile = get_object_or_404(UserProfile, user=user_id)
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project.save()
            return redirect(
                    'profiles:project_detail',
                    project_id=project_id
            )
    else:
        form = ProjectForm(instance=project)
    c = {
            "form": form,
            "project": project,
            "profile": profile
    }
    c.update(csrf(request))
    return render(request, "edit_project.jade", c)
