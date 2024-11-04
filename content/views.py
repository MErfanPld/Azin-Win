from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.utils.text import slugify
from unidecode import unidecode
from order.forms import OrderForm
from .filters import CategoryFilters, ContentFilters
from .helpers import type_content_CHOICES, status_content_CHOICES
from .models import Category, Content
from .forms import CategoryForm, ContentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator


# Create your views here.

class ContentUPVC(View):
    template_name = 'content/upvc.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = OrderForm()
        return render(request, self.template_name, context)


class ContentTermal(View):
    template_name = 'content/termal.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = OrderForm()
        return render(request, self.template_name, context)


class Contentnama(View):
    template_name = 'content/nama.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = OrderForm()
        return render(request, self.template_name, context)


class ContentListView(View):
    template_name = 'content/list_content.html'

    def get(self, request, *args, **kwargs):
        contents = Content.objects.filter(status='A').order_by('-created')
        context = {
            'form': OrderForm(),
            'type_content_name': '',
        }

        type_content = request.GET.get('type_content')
        if type_content:
            contents = contents.filter(type_content=type_content)
            context['type_content_name'] = dict(
                type_content_CHOICES).get(type_content, '')

        contents = ContentFilters(data=self.request.GET, queryset=contents).qs

        # Pagination
        paginator = Paginator(contents, 5)  # 10 محتوا در هر صفحه
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['contents'] = page_obj
        context['paginator'] = paginator
        context['page_obj'] = page_obj

        return render(request, self.template_name, context)


class ContentDetailView(View):
    template_name = 'content/detail_content.html'

    def get(self, request, c_id, c_slug):
        content = get_object_or_404(Content, id=c_id, slug=c_slug)
        context = {
            'content': content,
        }
        return render(request, self.template_name, context)


class ContentDashboardListView(ListView):
    model = Content
    template_name = 'content/admin/list.html'
    context_object_name = 'contents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contents = Content.objects.all()
        filtered_contents = ContentFilters(
            data=self.request.GET, queryset=contents).qs
        context['contents'] = filtered_contents
        # context['categories'] = Category.objects.all()
        context['status_types'] = status_content_CHOICES
        return context


class ContentDashboardCreateView(CreateView):
    model = Content
    template_name = 'content/admin/create_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('content:dashboard_content_list')


class ContentDashboardUpdateView(UpdateView):
    model = Content
    template_name = 'content/admin/create_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('content:dashboard_content_list')


class ContentDashboardDeleteView(DeleteView):
    model = Content
    template_name = 'content/admin/create_edit.html'
    success_url = reverse_lazy('content:dashboard_content_list')

# ========================= Category =========================


class CategoryListView(ListView):
    model = Category
    template_name = 'content/admin/category/list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contents = Category.objects.all()
        filtered_contents = CategoryFilters(
            data=self.request.GET, queryset=contents).qs
        context['categories'] = filtered_contents
        context['status_types'] = status_content_CHOICES
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'content/admin/category/create_edit.html'
    fields = ['title', 'slug','status']
    success_url = reverse_lazy('content:dashboard_category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'content/admin/category/create_edit.html'
    fields = ['title', 'slug','status']
    success_url = reverse_lazy('content:dashboard_category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'content/admin/category/list.html'
    success_url = reverse_lazy('content:dashboard_category_list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
