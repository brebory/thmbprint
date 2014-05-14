from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from badges.models import Badge

def list_badges(request):
    """
    Renders a page that lists all badges in the system.
    """
    badges = Badge.objects.all()
    c = { 'badges': badges }
    c.update(csrf(request))
    return render_to_response('badge_list.jade', c, RequestContext(request))

def badge_detail(request, badge_id):
    """
    Renders a badge-specific page with details about that badge.
    """
    badge = Badge.objects.get(pk=badge_id) 
    c = { 'badge': badge }
    c.update(csrf(request))
    return render_to_response('badge_detail.jade', c, RequestContext(request))
