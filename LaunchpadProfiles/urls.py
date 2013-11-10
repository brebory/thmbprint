from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'LaunchpadProfiles.views.home', name='home'),
    url(r'^login/$', 'LaunchpadProfiles.views.login', name='login'),
    url(r'^logout/$', 'LaunchpadProfiles.views.logout', name='logout'),
    url(r'^register/$', 'LaunchpadProfiles.views.register', name='register'),
    url(r'^about/$', 'LaunchpadProfiles.views.about', name='about'),
    url(r'^support/$', 'LaunchpadProfiles.views.support', name='support'),
    url(r'^explore/$', 'LaunchpadProfiles.views.explore', name='explore'),
    url(r'^resources/$', 'LaunchpadProfiles.views.resources', name='resources'),
    url(r'^user/', include('profiles.urls', namespace='profiles', app_name='profiles')),
    url(r'^badges/', include('badges.urls', namespace='badges', app_name='badges')),
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
