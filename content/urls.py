from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('upvc/', views.ContentUPVC.as_view(), name='home_upvc'),
    path('thermal_break/', views.ContentTermal.as_view(), name='home_termal'),
    path('curtain_wall/', views.Contentnama.as_view(), name='home_nama'),
    # path('<int:c_id>/<str:c_slug>', views.ContentDetailView.as_view(), name='home_detail_content'),
    # path('dashboard/create', views.ContentCreateView.as_view(), name='create_content'),
    # path('dashboard/content/list', views.ContentDashboardList.as_view(), name='list_content'),
    # path('dashboard/content/edit/<int:pk>', views.ContentUpdateView.as_view(), name='update_content'),
    # path('dashboard/content/delete/<int:pk>', views.ContentDashboardDelete.as_view(), name='delete_content'),
]
