from django import forms

from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ['created']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
