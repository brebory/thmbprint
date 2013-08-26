from django.shortcuts import render
from badges.models import Badge

def list_badges(request):
    return render(request, 'badges_list.jade')

def badge_detail(request, badge_id):
   badge = Badge.objects.get(pk=badge_id) 
   c = { 'badge': badge }
   return render(request, 'badge_detail.jade', c)
