import requests, json
from django.contrib import admin
from LaunchpadProfiles import settings
from badges.models import Badge, UserBadge, Assertion

class BadgeAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context={}):
        extra_context['credly_temp_token'] = self.get_credly_temp_token()
        return super(BadgeAdmin, self).add_view(request, form_url,
                extra_context)

    def change_view(self, request, object_id, form_url="", extra_context={}):
        extra_context['credly_temp_token'] = self.get_credly_temp_token()
        return super(BadgeAdmin, self).change_view(request, object_id,
                form_url, extra_context)

    def get_credly_temp_token(self):
        url = "https://credly.com/badge-builder/code"
        params = { 'access_token': settings.CREDLY_API_KEY }
        response = requests.post(url=url, params=params)
        print "Credly API Key: {0}".format(settings.CREDLY_API_KEY)
        print response.text
        resp_json = json.loads(response.text)

        return resp_json.get('temp_token', '')


admin.site.register(Badge, BadgeAdmin)
admin.site.register(UserBadge)
admin.site.register(Assertion)
