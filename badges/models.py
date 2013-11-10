from django.db import models
from profiles.models import UserProfile

class Badge(models.Model):
    """
    Class Badge represents badges in Thmbprint's system as well
    as storing a reference to the id of the Mozilla Open Badge that
    it corresponds to. Badges can be awarded to users, which will make
    a POST request to OpenBadges to award the Open Badge.

    @property name: The display name of the badge
    @property description: The long description of the badge
    @property users_set: The set of users who have obtained this badge
    @property image: The image of the badge itself
    @property achievement_key: key for the associated achievement
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_data = models.ImageField(upload_to='badges')
    achievement_key = models.CharField(max_length=50, default='dummy_achievement')

    def check_open_badge(self):
        """
        check_open_badge makes sure that this badge is registered with Mozilla
        @return boolean, true if registered, false if not
        """
        pass
        
    def award_badge(self, user):
        """
        award_badge awards the user this badge.

        @param user: the user to obtain the badge
        """
        UserBadge.objects.create(user=user, badge=self)


class UserBadge(models.Model):
    """
    Class UserBadge represents a user's own copy of a badge.

    @property user: Foreign key to the user that owns this badge
    @property badge: The badge that this UserBadge awards
    """
    user = models.ForeignKey(UserProfile)
    badge = models.ForeignKey(Badge)
