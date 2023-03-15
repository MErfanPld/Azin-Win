from django.urls import path, include
from . import views

# app_name = "about_us"

urlpatterns = [
    path('', views.AboutUsView.as_view(), name="about_us")
]
