from django.urls import path, include
from . import views

app_name = "top_projects"

urlpatterns = [
    path('', views.TopProjectListView.as_view(), name='home_list_top_projects'),
    path('dashboard/create', views.TopProjectCreateView.as_view(), name='create_top_projects'),
    path('dashboard/list', views.TopProjectDashboardList.as_view(), name='list_top_projects'),
    path('dashboard/edit/<int:pk>', views.TopProjectUpdateView.as_view(), name='update_top_projects'),
    path('dashboard/delete/<int:pk>', views.TopProjecDashboardDelete.as_view(), name='delete_top_projects'),
]
