from django import forms

from .models import About_us


class AboutForm(forms.ModelForm):
    class Meta:
        model = About_us
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
