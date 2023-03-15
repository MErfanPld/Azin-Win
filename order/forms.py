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


class OrderChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})
