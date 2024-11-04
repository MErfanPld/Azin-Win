from django.urls import path, include
from . import views

app_name = "about_us"

urlpatterns = [
    path('', views.AboutUsView.as_view(), name="about_us"),
    path('dashboard/create', views.AboutUsCreateView.as_view(), name='create_about'),
    path('dashboard/list', views.AboutUsDashboardList.as_view(), name='list_about'),
    path('dashboard/edit/<int:pk>', views.AboutUsUpdateView.as_view(), name='update_about'),
    path('dashboard/delete/<int:pk>', views.AboutUsDashboardDelete.as_view(), name='delete_about'),
]
