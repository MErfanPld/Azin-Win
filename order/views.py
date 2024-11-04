from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, DeleteView, ListView

from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from .filters import OrderFilters
from .helpers import type_project_CHOICES, status_CHOICES
from .models import Order, TypeWindow
from .forms import OrderForm, OrderChangeStatusForm
from content.models import Content


# Create your views here.


def test_map_ir(request):
    context = {
        'form': OrderForm()
    }
    return render(request, 'test_map_ir.html', context)


def test_show_map_ir(request):
    context = {
        'form': OrderForm(instance=Order.objects.last())
    }
    return render(request, 'test_map_ir.html', context)


def test_submit_order_angular_js(request):
    context = {
        'form': OrderForm()
    }

    print('wwwwwwwwwwwwwwwwwwww')
    print(Order.objects.count())

    return render(request, 'test_submit_order_angular_js.html', context)


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
            obj = new_order.save()

            sms_text = SMS_TEXTS['order_message']
            send_sms(new_order.phone_number, sms_text, new_order.full_name)
            messages.success(request,
                             f"کاربر گرامی درخواست شما با موفقیت ثبت شد و همکاران ما تا ساعاتی دیگر با شما تماس خواهند گرفت. برای مشاهده سفارشات خود ثبت نام بکنید.")

            return redirect('order:order_home')
        return render(request, 'order/front/home.html', {'form': form})


# ===================== Dashboard View =====================


class Dashboard(LoginRequiredMixin, View):
    template_name = 'order/admin/dashboard.html'

    def get(self, request, *args, **kwargs):
        orders = Order.objects.order_by('-id')
        if not request.user.is_staff:
            orders = orders.filter(phone_number=request.user.phone_number)
        contents = Content.objects.order_by('-id')
        context = {'orders': orders, 'contents': contents}
        return render(request, self.template_name, context)


class OrderDashboardList(LoginRequiredMixin, View):
    template_name = 'order/admin/order.html'

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        if not request.user.is_staff:
            orders = orders.filter(phone_number=request.user.phone_number)
        orders = OrderFilters(data=self.request.GET, queryset=orders).qs
        type_windows = TypeWindow.objects.all()
        type_projects = type_project_CHOICES
        status_types = status_CHOICES
        context = {'orders': orders, 'type_windows': type_windows, 'type_projects': type_projects,
                   'status_types': status_types, 'change_status_form': OrderChangeStatusForm()}
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


class OrderDashboardDelete(DeleteView):
    model = Order
    template_name = 'order/admin/order.html'
    success_url = reverse_lazy('order:dashboard_order_list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


# PDF
class OrderPDFView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/pdf.html'
    queryset = Order.objects.all()



import openpyxl
from django.http import HttpResponse
from django.views import View
from .models import Order

class ExportOrdersToExcelView(View):
    def get(self, request, *args, **kwargs):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Orders"
        headers = [
            "نام و نام خانوادگی", 
            "شماره تماس", 
            "نوع پنجره", 
            "نوع پروژه", 
            "تعداد واحد", 
            "شهر", 
            "وضعیت درخواست", 
            "زمان ساخت"
        ]
        sheet.append(headers)
        orders = Order.objects.all()
        for order in orders:
            row = [
                order.full_name,
                order.phone_number,
                order.type_window.name if order.type_window else "",
                order.get_type_project_display(),
                order.number,
                order.get_citys_display(),
                order.get_status_display(),
                order.created.strftime("%Y-%m-%d %H:%M:%S"),
            ]
            sheet.append(row)
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment; filename=orders.xlsx"
        workbook.save(response)
        return response
