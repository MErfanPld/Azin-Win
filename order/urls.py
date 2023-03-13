from django.urls import path, include
from . import views

app_name = "order"

urlpatterns = [
    path('', views.OrderCreateView.as_view(), name='order_home'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/order/list/', views.OrderDashboardList.as_view(), name='dashboard_order_list'),
    path('dashboard/order/<int:o_id>/', views.OrderDashboardDetail.as_view(), name='dashboard_order_detail'),
]
