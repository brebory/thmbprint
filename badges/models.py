from django.db import models
from profiles.models import UserProfile

class Badge(models.Model):
    name = models.CharField()
    description = models.TextField()
    users_set = models.ManyToManyField(UserProfile)
    image_data = models.ImageField()
