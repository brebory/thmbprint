from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views',
        url(r'(?P<user_id>\d+)/$', 'dashboard'),
        url(r'(?P<user_id>\d+)/project/$', 'list_projects'),
        url(r'(?P<user_id>\d+)/project/create/$', 'create_project'),
        url(r'(?P<user_id>\d+)/project/(?P<project_id>\d+)/$',
            'project_detail'),
)
