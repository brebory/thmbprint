from django.conf.urls import patterns, include, url

urlpatterns = patterns('badges.views',
        url(r'^$', 'list_badges', name='list_badges'),
        url(r'(?P<badge_id>\d+)/$', 'badge_detail', name='badge_detail'),
)
