from django.shortcuts import render_to_response
from badges.models import Badge

def list_badges(request):
    """
    Renders a page that lists all badges in the system.
    """
    badges = Badge.objects.all()
    c = { 'badges': badges }
    return render_to_response('badge_list.jade', c)

def badge_detail(request, badge_id):
    """
    Renders a badge-specific page with details about that badge.
    """
    badge = Badge.objects.get(pk=badge_id) 
    c = { 'badge': badge }
    return render_to_response('badge_detail.jade', c)
