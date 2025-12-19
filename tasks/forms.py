from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["is_done", "content", "tag_ids", "deadline_date", ]
        widgets = {
            "tag_ids": forms.CheckboxSelectMultiple(attrs={}),
            "deadline_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
