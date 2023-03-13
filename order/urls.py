from django.urls import path, include
from . import views

app_name = "order"

urlpatterns = [
    # TODO remove this line after approval
    path('test_map_ir', views.test_map_ir, name='test_map_ir'),

    path('', views.OrderCreateView.as_view(), name='order_home'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/order/list/', views.OrderDashboardList.as_view(), name='dashboard_order_list'),
    path('dashboard/order/<int:o_id>/', views.OrderDashboardDetail.as_view(), name='dashboard_order_detail'),
]
