from django.urls import path, include
from . import views

app_name = "order"

urlpatterns = [
    path('', views.OrderCreateView.as_view(), name='order_home'),
]
