from django import forms

from .models import TopProject


class TopProjectForm(forms.ModelForm):
    class Meta:
        model = TopProject
        exclude = ['created']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
