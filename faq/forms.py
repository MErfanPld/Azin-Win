from django import forms

from .models import FAQ


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
