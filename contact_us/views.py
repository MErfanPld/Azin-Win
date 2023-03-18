from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from .filters import ContactUsFilters
from .forms import ContactUsForm
from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from .models import ContactUs
from .helpers import status_CHOICES


# Create your views here.


class ContactUsView(View):
    form_class = ContactUsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'contact_us/contact_us.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            obj = new_order.save()

            sms_text = SMS_TEXTS['order_message'].format(new_order.full_name)
            send_sms(new_order.phone_number, sms_text)
            messages.success(request,
                             f"کاربر گرامی پیام شما با موفقیت ثبت شد و پس از بررسی با شما تماس گرفته خواهد شد.")

            return redirect('order:order_home')
        return render(request, 'contact_us/contact_us.html', {'form': form})


class ContactDashboard(LoginRequiredMixin, View):
    template_name = 'contact_us/admin/list.html'

    def get(self, request, *args, **kwargs):
        context = {}

        contact_us = ContactUs.objects.all()
        contact_us = ContactUsFilters(data=self.request.GET, queryset=contact_us).qs
        context['status_types'] = status_CHOICES
        context['contact_us'] = contact_us
        return render(request, self.template_name, context)


class ContactDashboardDelete(DeleteView):
    model = ContactUs
    template_name = 'contact_us/admin/list.html'
    success_url = reverse_lazy('contact_us:dashboard_contact_us')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
