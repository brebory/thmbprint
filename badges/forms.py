from django.forms import ModelForm, Textarea
from badges.models import Badge

class BadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ('name', 'description', 'image_data', 'achievement_key')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
