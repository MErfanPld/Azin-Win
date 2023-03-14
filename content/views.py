from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify


from .models import Content
from .forms import ContentForm

# Create your views here.

class ContentListView(View):
    template_name = 'content/list_content.html'

    def get(self, request, *args, **kwargs):
        contents = Content.objects.filter(status='A')
        context = {'contents': contents}
        return render(request, self.template_name, context)


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/detail_content.html'

    def setup(self, request, *args, **kwargs):
        self.content_instance = get_object_or_404(Content, pk=kwargs['c_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        contents = Content.objects.filter(status='A')
        return render(request, self.template_name,
                      {'content': self.content_instance})



class ContentCreateView(View):
    form_class = ContentForm
    template_name = 'content/admin/create_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.slug = slugify(form.cleaned_data['title'][:30])
            new_content.save()
            messages.success(request, 'محتوا با موفقیت ثبت شد.', 'success')
            return redirect('content:list_content')
        return render(request, self.template_name, {'form': form})


class ContentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ContentForm
    template_name = 'content/admin/create_edit.html'

    def setup(self, request, *args, **kwargs):
        self.content_instance = get_object_or_404(Content, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.content_instance
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.content_instance
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.content_instance
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.slug = slugify(form.cleaned_data['title'][:30])
            new_content.user = request.user
            new_content.save()
            return redirect('content:list_content')
        return render(request, self.template_name, {'form': form})


class ContentDashboardList(LoginRequiredMixin, View):
    template_name = 'content/admin/list.html'

    def get(self, request, *args, **kwargs):
        contents = Content.objects.all()
        context = {'contents': contents}
        return render(request, self.template_name, context)

