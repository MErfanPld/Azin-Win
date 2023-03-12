from django.shortcuts import redirect, render
from django.views import View

from .models import Content
from .forms import ContentForm

# Create your views here.

class ContentCreateView(View):
    form_class = ContentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'content/create_edit.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.save()
            return redirect('content:create_content', new_content.id)
