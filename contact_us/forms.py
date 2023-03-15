from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['created']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
