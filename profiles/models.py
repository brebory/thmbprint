from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import hashlib
import datetime

def generate_upload_path(instance, filename):
    # Generate filename by md5 hashing previous filename and the current time
    filehash = hashlib.md5()
    filehash.update(instance.name.replace(" ", "-"))
    filehash.update(str(datetime.datetime.now()))
    return '/'.join(
            ['content', 
             instance.project.profile.user.username,
             filehash.hexdigest() + "." +
             instance.attached_file_extension]
    )

class UserProfile(models.Model):
    """
    Class UserProfile represents special information about a user beyond the
    basic information that Django's User model collects. This is abstracted out
    into a separate class and linked to Django's User model with a
    OneToOneField relation.

    @property user: The related django.contrib.auth.models.User object

    TODO: Create more useful fields for users to customize, like profile
    pictures, location information, school/work information, etc.
    """

    user = models.OneToOneField(User)

    def __unicode__(self):
        if self.user:
            return self.user.username
        return "unassigned userprofile: %s" % self.pk

class StudentUser(models.Model):
    """
    Class StudentUser creates a Student account for the associated UserProfile.
    Student accounts and mentor accounts have access to different aspects of
    Thmbprint. As of now, this feature is not implemented.

    @property profile: The related profiles.models.UserProfile object

    TODO: Finish implementing Student vs Mentor users.
    """

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
