from profiles.models import UserProfile, Project

class DummyAchievement(object):
    name = "Dummy Achievement"
    key = "dummy_achievement"
    description = "This is a default dummy achievement!"
    bonus = 0

    def evaluate(self, user, *args, **kwargs):
        """
        It's impossible to get this achievement, always return False.
        """
        return False

class SignUpAchievement(object):
    name = "Signed Up"
    key = "signup"
    description = "You created an account on Thmbprint!"
    bonus = 10

    def evaluate(self, user, *args, **kwargs):
        """
        If the user is registered, they've unlocked this achievement.
        """
        return user.is_authenticated()
    
class FirstProjectAchievement(object):
    name = "First Steps"
    key = "1project"
    description = "You've created one project on Thmbprint!"
    bonus = 10

    def evaluate(self, user, *args, **kwargs):
        """
        If the user has created at least one project, they've unlocked this
        achievement.
        """
        profile = UserProfile.objects.get(user = user)
        return profile and profile.project_set.count() >= 1

class FiveProjectsAchievement(object):
    name = "Next Steps"
    key = "5project"
    description = "You've created five projects on Thmbprint!"
    bonus = 20

    def evaluate(self, user, *args, **kwargs):
        """
        If the user has created at least five projects, they've unlocked this
        achievement.
        """
        profile = UserProfile.objects.get(user = user)
        return profile and profile.project_set.count() >= 5
