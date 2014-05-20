from django import template

register = template.Library()

def getbadgeinstance(badgelist, achievementid):
    return badgelist.get(achievement_key = achievementid).name

register.simple_tag(getbadgeinstance)
