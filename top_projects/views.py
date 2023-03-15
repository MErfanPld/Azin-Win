from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from .filters import TopFilters
from .helpers import status_content_CHOICES
from .models import TopProject
from .forms import TopProjectForm


# Create your views here.

class TopProjectListView(View):
    template_name = 'top_projects/list_top_project.html'

    def get(self, request, *args, **kwargs):
        top_projects = TopProject.objects.filter(status='A')
        context = {'top_projects': top_projects}

        return render(request, self.template_name, context)


class TopProjectCreateView(View):
    form_class = TopProjectForm
    template_name = 'top_projects/admin/create_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_top_projects = form.save(commit=False)
            new_top_projects.slug = slugify(form.cleaned_data['title'][:30])
            new_top_projects.save()
            messages.success(request, 'محتوا با موفقیت ثبت شد.', 'success')
            return redirect('top_projects:list_top_projects')
        return render(request, self.template_name, {'form': form})


class TopProjectUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TopProjectForm
    template_name = 'top_projects/admin/create_edit.html'

    def setup(self, request, *args, **kwargs):
        self.top_projects = get_object_or_404(TopProject, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.top_projects
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.top_projects
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.top_projects
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_top_projects = form.save(commit=False)
            new_top_projects.slug = slugify(form.cleaned_data['project_name'][:30])
            new_top_projects.user = request.user
            new_top_projects.save()
            return redirect('top_projects:list_top_projects')
        return render(request, self.template_name, {'form': form})


class TopProjectDashboardList(LoginRequiredMixin, View):
    template_name = 'top_projects/admin/list.html'

    def get(self, request, *args, **kwargs):
        top_projects = TopProject.objects.all()
        context = {'top_projects': top_projects}
        return render(request, self.template_name, context)
