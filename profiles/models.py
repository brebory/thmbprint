from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
import hashlib
import datetime

EXTENSION_CHOICES = (
    ('pdf', 'pdf'),
    ('png', 'png'),
    ('jpg', 'jpg'),
    ('txt', 'txt')
)

VALID_EXTENSIONS = (
    'pdf',
    'png',
    'jpg',
    'txt'
)

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

def validate_file_extension(file_object):
    extension = file_object.name.split(".")[-1]
    if extension not in VALID_EXTENSIONS:
        raise ValidationError(
            "%s is not a valid extension" % extension,
            'invalid_extension'
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

    def is_owned_by(self, user):
        return user.project_set.filter(pk=self.pk).exists()

class ProjectItem(models.Model):
    """
    Class ProjectItem represents one part of a project. This can be anything
    from a text document, to a pdf, to an image, and the user can title
    these parts as well as give them a short description of the contents.

    @property project: The related Project object
    @property name: The name of this ProjectItem
    @property description: A short description of this ProjectItem
    @property attached_file: The file object to be stored with the ProjectItem
    @property attached_file_extension: The extension of the attached file
    """

    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attached_file = models.FileField(
            validators = [validate_file_extension],
            upload_to = generate_upload_path,
            blank = True,
            null = True
    )

    attached_file_extension = models.CharField(
            max_length=4,
            choices=EXTENSION_CHOICES,
            blank = True
    )

    def save(self, *args, **kwargs):
        """
        Automatically gets the attached_file_extension from the passed in
        file's name. Removes the need for the user to specify the attached file
        extension in the ModelForm.

        Overrides the default models.Model save function.
        """

        attached_file_extension = attached_file.name.split('.')[-1]
        super(ProjectItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Recommendation(models.Model):
    student = models.ForeignKey(StudentUser)
    mentor = models.ForeignKey(MentorUser)
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.subject
