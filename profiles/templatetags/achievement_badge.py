from django import template

register = template.Library()

def getbadgeinstance(badgelist, achievementid):
    return badgelist.get(achievement_key = achievementid).name

def getbadgeurl(badgelist, key):
    return badgelist.get(achievement_key = key).image_data.url

register.simple_tag(getbadgeinstance)
register.simple_tag(getbadgeurl)
