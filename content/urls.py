from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('dashboard/create', views.ContentCreateView.as_view(), name='create_content'),
    path('dashboard/content/list', views.ContentDashboardList.as_view(), name='list_content'),
    path('dashboard/content/edit/<int:pk>', views.ContentUpdateView.as_view(), name='update_content'),
]
