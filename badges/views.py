import json
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from badges.models import Badge, UserBadge

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
    badge = get_object_or_404(Badge, pk=badge_id)
    c = { 'badge': badge }
    c.update(csrf(request))
    return render_to_response('badge_detail.jade', c, RequestContext(request))

def badge_json(request, badge_id):
    """
    Returns a json response for a badge url
    @param request: Django HttpRequest object
    @param badge_id: PK of the badge to obtain
    @return: application/json HttpResponse for badge object
    """
    badge = get_object_or_404(Badge, pk=badge_id)
    return HttpResponse(badge.to_json(), content_type="application/json")

def assertion_detail(request, badge_id, user_id):
    """
    Returns an Assertion for the specified Badge and User.
    @param request: Django HttpRequest view param
    @param badge_id: id of the Badge to get the associated Assertion
    @param user_id: id of the User to get the associated Assertion
    @return:
    """
    userbadge = get_object_or_404(UserBadge, user=user_id, badge=badge_id)
    if userbadge.assertion:
        return HttpResponse(userbadge.assertion.to_json(), content_type="application/json")
    else:
        raise Http404

def organization_info(request):
    """
    Returns a json response of information about this organization
    @param request: Django HttpRequest object
    @return: application/json mimetype metadata about organization
    """

    data = {
        "name": "Thmbprint",
        "description": "Professional portfolios and career-building for students.",
        "url": "http://thmbprint.herokuapp.com",
        "email": "hydepark@gmail.com",
        "revocationList": []
    }
    return HttpResponse(json.dumps(data), content_type="application/json")