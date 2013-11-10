from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from profiles.models import Project, ProjectItem, ProjectItemFile

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

ProjectItemFormset = inlineformset_factory(
        Project,
        ProjectItem,
        max_num = 10,
        extra = 1
)

ProjectItemFileFormset = inlineformset_factory(
        ProjectItem,
        ProjectItemFile,
        max_num = 3,
        extra = 1
)
