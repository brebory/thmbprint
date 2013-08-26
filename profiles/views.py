from django.shortcuts import render
from profiles.models import UserProfile, StudentUser, MentorUser
from profiles.models import Project, ProjectItem
from profiles.models import ProjectItemImage, ProjectItemFile, Recommendation
from profiles.forms import ProjectForm

def dashboard(request, user_id):
    profile = UserProfile.objects.get(user=user_id)
    c = { "profile": profile }
    return render(request, 'dashboard.jade', c)

def list_projects(request, user_id):
    profile = UserProfile.objects.jget(user=user_id)
    projects = profile.project_set
    c = {"profile": profile, "projects": projects}
    return render(request, 'list_projects.jade', c)

def create_project(request, user_id):
    if request.method == 'POST':
        profile = UserProfile.objects.get(user=user_id)
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

def project_detail(request, user_id, project_id):
    profile = UserProfile.objects.get(user=user_id)
    project = Project.objects.get(pk=project_id)
    c = { "profile": profile,
          "project": project,
          "editable": (project in profile.project_set) }
