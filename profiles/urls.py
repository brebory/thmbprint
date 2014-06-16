from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views',
        url(r'dashboard/$', 'dashboard', name='dashboard'),
        url(
            r'project/$', 
            'list_user_projects',
            name='list_user_projects'
        ),
        url(
            r'project/create/$',
            'create_project',
            name='create_project'
        ),
        url(
            r'project/(?P<project_id>\d+)/$',
            'project_detail',
            name='project_detail'
        ),
        url(
            r'project/(?P<project_id>\d+)/edit/$',
            'edit_project',
            name='edit_project'
        ),
	url(
	    r'migrate-achievements/$',
            'migrate_achievements',
            name='migrate_achievements'
        ),
)
