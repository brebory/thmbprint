from django.contrib import admin
from profiles.models import UserProfile, StudentUser, MentorUser
from profiles.models import Project, ProjectItem, Recommendation

admin.site.register(UserProfile)
admin.site.register(StudentUser)
admin.site.register(MentorUser)
admin.site.register(Project)
admin.site.register(ProjectItem)
admin.site.register(Recommendation)
