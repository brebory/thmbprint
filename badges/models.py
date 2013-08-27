from django.db import models
from profiles.models import UserProfile

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users_set = models.ManyToManyField(UserProfile, blank=True, null=True)
    image_data = models.ImageField(upload_to='badges')
