from django.conf.urls import patterns, include, url

urlpatterns = patterns('badges.views',
        url(r'^$', 'list_badges', name='list_badges'),
        url(r'(?P<badge_id>\d+)/$', 'badge_detail', name='badge_detail'),
        url(r'(?P<badge_id>\d+)\.json$', 'badge_json', name='badge_json'),
        url(r'assertion/(?P<badge_id>\d+)/user/(?P<user_id>\d+)/$', 'assertion_detail', name='assertion_detail'),
        url(r'organization.json', 'organization_info', name='organization_info'),
)
