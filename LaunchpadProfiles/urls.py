from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LaunchpadProfiles.views.home', name='home'),
    # url(r'^LaunchpadProfiles/', include('LaunchpadProfiles.foo.urls')),
    url(r'^$', 'LaunchpadProfiles.views.home', name='home'),
    url(r'^login/$', 'LaunchpadProfiles.views.login', name='login'),
    url(r'^register/$', 'LaunchpadProfiles.views.register', name='register'),
    url(r'^register/$', 'LaunchpadProfiles.views.about', name='about'),
    url(r'^support/$', 'LaunchpadProfiles.views.support', name='support'),
    url(r'^user/$', include('profiles.urls')),
    url(r'^badges/$', include('badges.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
