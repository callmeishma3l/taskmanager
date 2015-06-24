from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ()#'date_added','last_modified',)

        widgets = {
            'deadline': forms.TextInput(attrs={'class': 'datepicker'}),
        }