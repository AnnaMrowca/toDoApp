from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('creation_date', 'completion_date', 'user')