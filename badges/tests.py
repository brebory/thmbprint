"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from badges.models import Badge, UserBadge, UserOpenBadge

class SimpleTest(TestCase):
    def setUp(self):
        pass