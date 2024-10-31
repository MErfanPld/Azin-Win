from django import forms

from .models import Content, Category


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'slug', 'category',
                  'body', 'cover', 'thumbnail', 'status']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Content.objects.filter(slug=slug).exists():
            raise forms.ValidationError("این slug قبلاً استفاده شده است.")
        return slug


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'status']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Content.objects.filter(slug=slug).exists():
            raise forms.ValidationError("این slug قبلاً استفاده شده است.")
        return slug
