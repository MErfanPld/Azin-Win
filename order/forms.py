from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['created']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'lat': forms.HiddenInput(),
            'long': forms.HiddenInput(),
        }
