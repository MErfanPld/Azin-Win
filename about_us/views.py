from django.shortcuts import render
from django.views import View

from .models import About_us


# Create your views here.

class AboutUsView(View):
    template_name = 'about_us/about_us.html'

    def get(self, request, *args, **kwargs):
        about_us = About_us.objects.all()
        context = {'about_us': about_us}

        return render(request, self.template_name, context)
