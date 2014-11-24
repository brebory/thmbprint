import json
import hashlib
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from profiles.models import UserProfile
from django.contrib.sites.models import get_current_site


class Badge(models.Model):
    """
    Class Badge represents badges in Thmbprint's system. Each Badge has
    several associated UserBadge objects, as well as several associated
    Assertion objects, which represent individual instances of Badges
    that each User has collected, and possibly pushed to the OpenBadges API.

    @property name: The display name of the badge
    @property description: The long description of the badge
    @property users_set: The set of users who have obtained this badge
    @property image: The image of the badge itself
    @property achievement_key: key for the associated achievement
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_data = models.ImageField(upload_to='badges', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    achievement_key = models.CharField(max_length=50, default='dummy_achievement')

    def get_absolute_url(self):
        """
         Returns the absolute url to the object
        """

        return reverse('badges:badge_detail', args=[str(self.id)])

    def to_json(self):
        """
        Returns a json representation of a badge according to the OBI specifications
        """

        badge_url = ''.join(['http://', get_current_site(None).domain, self.get_absolute_url()])
        issuer_url = ''.join(['http://', get_current_site(None).domain, reverse('badges:organization_info')])
        data = {
            'name': self.name,
            'description': self.description,
            'image': self.image_data.url,
            'criteria': badge_url,
            'issuer': issuer_url,
            'alignment': [],
            'tags': ""
        }

        return json.dumps(data)


class UserBadge(models.Model):
    """
    Class UserBadge represents a user's own copy of a badge.

    @property user: Foreign key to the user that owns this badge
    @property badge: The badge that this UserBadge awards
    """
    user = models.ForeignKey(UserProfile)
    badge = models.ForeignKey(Badge)
    created_at = models.TimeField(auto_now_add=True)


class Assertion(models.Model):
    """
    Class Assertion represents a hosted OpenBadge object. Provides the metadata for the assertion endpoint
    for the OpenBadges API to verify validity of the assertion.

    It's the class that actually connects to the OpenBadges API and sends an assertion to the OpenBadges endpoint.
    @property userbadge = the associated UserBadge object
    """
    userbadge = models.OneToOneField(UserBadge)

    def get_absolute_url(self):
        return reverse('badges:assertion_detail', args=[str(self.id)])


    def to_json(self):
        """
        Returns a json representation of an Assertion according to the OBI specifications

        TODO: Make this not crash if the user doesn't have an associated email address
        """
        sha = hashlib.sha256()
        sha.update(self.userbadge.user.user.email)
        identity_hash = "sha256$" + sha.digest()

        badge_url = ''.join(['http://', get_current_site(None).domain, self.userbadge.badge.get_absolute_url()])
        assertion_url = ''.join(['http://', get_current_site(None).domain, self.get_absolute_url()])

        data = {
            'uid': self.pk,
            'recipient': {
                'identity': identity_hash,
                'type': 'email',
                'hashed': True
            },
            'badge': badge_url,
            'verify': {
                'type': 'hosted',
                'url': assertion_url
            },
            'issuedOn': self.userbadge.created_at
        }

        return json.dumps(data)

def postAssertion(badge):
    """
    postOpenBadge makes a POST request to the OpenBadges API, POSTing a new badge object to
    their servers.
    @param badge:
    @return:
    """
    pass

post_save.connect(Assertion, postAssertion)