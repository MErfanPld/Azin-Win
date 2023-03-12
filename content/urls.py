from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('create', views.ContentCreateView.as_view(), name='create_content'),
]
