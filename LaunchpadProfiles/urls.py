from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LaunchpadProfiles.views.home', name='home'),
    # url(r'^LaunchpadProfiles/', include('LaunchpadProfiles.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
