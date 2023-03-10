from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView

from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from .models import Order
from .forms import OrderForm
from content.models import Content


# Create your views here.


def test_map_ir(request):
    return render(request, 'test_map_ir.html')

def home(request):
    return render(request, 'order/home.html')


class OrderCreateView(View):
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'order/front/home.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.save()

            sms_text = SMS_TEXTS['order_message'].format(new_order.full_name)
            send_sms(new_order.phone_number, sms_text)
            messages.success(request,
                             f"کاربر گرامی درخواست شما با موفقیت ثبت شد و پس از بررسی با شما تماس گرفته خواهد شد.")

            return redirect('order:order_home')
        return render(request, 'order/front/home.html', {'form': form})


# ===================== Dashboard View =====================


class Dashboard(LoginRequiredMixin, View):
    template_name = 'order/admin/dashboard.html'

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        contents = Content.objects.all()
        context = {'orders': orders, 'contents': contents}
        return render(request, self.template_name, context)


class OrderDashboardList(LoginRequiredMixin, View):
    template_name = 'order/admin/order.html'

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        context = {'orders': orders}
        return render(request, self.template_name, context)


class OrderDashboardDetail(DetailView):
    model = Order

    def setup(self, request, *args, **kwargs):
        self.order_instance = get_object_or_404(Order, pk=kwargs['o_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        return render(request, 'order/admin/detail_order.html',
                      {'order': self.order_instance})
