from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from profiles.models import Project, ProjectItem

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

class ProjectItemForm(ModelForm):
    class Meta:
        model = ProjectItem
        

ProjectItemFormset = inlineformset_factory(
        Project,
        ProjectItem,
        max_num = 10,
        extra = 1
)
