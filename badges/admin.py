from django.contrib import admin
from badges.models import Badge, UserBadge, Assertion

admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(Assertion)
