from django.urls import path, include
from . import views

app_name = "contact_us"

urlpatterns = [
    path('', views.ContactUsView.as_view(), name="contact_us"),
    path('dashboard/contact/list/', views.ContactDashboard.as_view(), name="dashboard_contact_us"),
    path('dashboard/contact/delete/<int:pk>', views.ContactDashboardDelete.as_view(), name="dashboard_contact_us_delete"),
]
