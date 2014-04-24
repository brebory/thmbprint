from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

def generate_upload_path(instance, filename):
    return '/'.join(
            ['content', 
             instance.project.profile.user.username,
             instance.name.replace(" ", "_") + "." +
             instance.attached_file_extension]
    )

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
    EXTENSION_CHOICES = ( 
            ('doc', 'doc'),
            ('pdf', 'pdf'),
            ('png', 'png'),
            ('jpg', 'jpg'),
            ('txt', 'txt')
    )
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attached_file = models.FileField(
            upload_to = generate_upload_path,
            blank = True,
            null = True
    )
    attached_file_extension = models.CharField(
            max_length=4,
            choices=EXTENSION_CHOICES
    )

    def __unicode__(self):
        return self.name

class Recommendation(models.Model):
    student = models.ForeignKey(StudentUser)
    mentor = models.ForeignKey(MentorUser)
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.subject
