from django.shortcuts import render
from django.views import View

from about_us.forms import AboutForm

from .models import About_us
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

# Create your views here.


class AboutUsView(View):
    template_name = 'about_us/about_us.html'

    def get(self, request, *args, **kwargs):
        about_us = About_us.objects.all()
        context = {'about_us': about_us}

        return render(request, self.template_name, context)


class AboutUsCreateView(View):
    form_class = AboutForm
    template_name = 'about_us/admin/create_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_AboutUs = form.save(commit=False)
            new_AboutUs.save()
            messages.success(request, 'محتوا با موفقیت ثبت شد.', 'success')
            return redirect('AboutUs:list_AboutUs')
        return render(request, self.template_name, {'form': form})


class AboutUsUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AboutForm
    template_name = 'about_us/admin/create_edit.html'

    def setup(self, request, *args, **kwargs):
        self.AboutUss = get_object_or_404(About_us, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.AboutUss
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.AboutUss
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.AboutUss
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_AboutUs = form.save(commit=False)
            new_AboutUs.user = request.user
            new_AboutUs.save()
            return redirect('AboutUs:list_AboutUs')
        return render(request, self.template_name, {'form': form})


class AboutUsDashboardDelete(DeleteView):
    model = About_us
    template_name = 'about_us/admin/list.html'
    success_url = reverse_lazy('AboutUs:list_AboutUs')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class AboutUsDashboardList(LoginRequiredMixin, View):
    template_name = 'about_us/admin/list.html'

    def get(self, request, *args, **kwargs):
        AboutUss = About_us.objects.all()
        context = {'AboutUss': AboutUss}
        return render(request, self.template_name, context)
