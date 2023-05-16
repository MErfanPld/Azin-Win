from django.shortcuts import render
from django.views import View
from .models import FAQ
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from .forms import FAQForm


# Create your views here.

class FAQListView(View):
    template_name = 'faq/faq.html'

    def get(self, request, *args, **kwargs):
        faqs = FAQ.objects.all()
        context = {'faqs': faqs}

        return render(request, self.template_name, context)


class FAQCreateView(View):
    form_class = FAQForm
    template_name = 'faq/admin/create_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_faq = form.save(commit=False)
            # new_faq.slug = slugify(form.cleaned_data['project_name'])
            new_faq.save()
            messages.success(request, 'سوال با موفقیت ثبت شد.', 'success')
            return redirect('faq:list_faq')
        return render(request, self.template_name, {'form': form})


class FAQUpdateView(LoginRequiredMixin, UpdateView):
    form_class = FAQForm
    template_name = 'faq/admin/create_edit.html'

    def setup(self, request, *args, **kwargs):
        self.faqs = get_object_or_404(FAQ, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.faqs
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.faqs
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.faqs
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_faq = form.save(commit=False)
            new_faq.user = request.user
            new_faq.save()
            return redirect('faq:list_faq')
        return render(request, self.template_name, {'form': form})


class FAQDashboardDelete(DeleteView):
    model = FAQ
    template_name = 'faq/admin/list.html'
    success_url = reverse_lazy('faq:list_faq')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class FAQDashboardList(LoginRequiredMixin, View):
    template_name = 'faq/admin/list.html'

    def get(self, request, *args, **kwargs):
        faqs = FAQ.objects.all()
        context = {'faqs': faqs}
        return render(request, self.template_name, context)
