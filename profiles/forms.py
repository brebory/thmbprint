from django.forms import ModelForm
from profiles.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['profile', 'name', 'description', 'start_date', 'end_date']

