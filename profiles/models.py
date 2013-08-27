from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

def generate_upload_path(instance, filename):
    return '/'.join('content', instance.project_item.project.profile.username)

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    def __unicode__(self):
        if self.user:
            return self.user.username
        return "unassigned userprofile: %s" % self.pk

class StudentUser(models.Model):

    profile = models.ForeignKey(
            UserProfile,
            blank=True,
            null=True,
            unique=True,
            related_name="student_profile"
    )

    def __unicode__(self):
        if self.profile:
            return self.profile.__unicode__()
        return "unassigned studentuser: %s" % self.pk

class MentorUser(models.Model):

    profile = models.ForeignKey(
            UserProfile,
            blank=True,
            null=True,
            unique=True,
            related_name="mentor_profile"
    )

    def __unicode__(self):
        if self.profile:
            return self.profile.__unicode__()
        return "unassigned mentoruser:%s" % self.pk

class Project(models.Model):
    profile = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    def __unicode__(self):
        return self.name

class ProjectItem(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class ProjectItemImage(models.Model):
    project_item = models.ForeignKey(ProjectItem)
    url = models.URLField()
    image_data = models.ImageField(upload_to=generate_upload_path)

    def __unicode__(self):
        return self.url

class ProjectItemFile(models.Model):
    project_item = models.ForeignKey(ProjectItem)
    url = models.URLField()
    file_data = models.FileField(upload_to=generate_upload_path)

    def __unicode__(self):
        return self.url
    
class Recommendation(models.Model):
    student = models.ForeignKey(StudentUser)
    mentor = models.ForeignKey(MentorUser)
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.subject
