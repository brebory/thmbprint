from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20)
    first_name = models.CharField()
    last_name = models.CharField()

class StudentUser(models.Model):
    profile = models.ForeignKey(UserProfile)

class MentorUser(models.Model):
    profile = models.ForeignKey(UserProfile)

class Project(models.Model):
    profile = models.ForeignKey(UserProfile)
    name = models.CharField()
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

class ProjectItem(models.Model):
    project = models.ForeignKey(Project)
    description = models.TextField(blank=True)

class ProjectItemImage(models.Model):
    project_item = models.ForeignKey(ProjectItem)
    url = models.URLField()
    image_data = models.ImageField()

class ProjectItemFile(models.Model):
    project_item = models.ForeignKey(ProjectItem)
    url = models.URLField()
    file_data = models.FileField()
    
class Recommendation(models.Model):
    student = models.ForeignKey(StudentUser)
    mentor = models.ForeignKey(MentorUser)
