from django.forms import ModelForm
from badges.models import Badge

class BadgeForm(ModelForm):
    class Meta:
        model = Badge

