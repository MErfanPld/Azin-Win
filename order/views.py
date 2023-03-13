from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.utils.text import slugify

from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from .models import Order
from .forms import OrderForm

# Create your views here.


def home(request):
    return render(request, 'order/home.html')


class OrderCreateView(View):
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'order/home.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.save()
            sms_text = SMS_TEXTS['order_message'].format(new_order.full_name)
            send_sms(new_order.phone_number, sms_text)
            return redirect('order:order_home', new_order.id)
        return render(request, 'order/home.html', {'form': form})
