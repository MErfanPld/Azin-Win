from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('upvc/', views.ContentUPVC.as_view(), name='home_upvc'),
    path('thermal_break/', views.ContentTermal.as_view(), name='home_termal'),
    path('curtain_wall/', views.Contentnama.as_view(), name='home_nama'),

    path('contents/', views.ContentListView.as_view(), name='home_list_content'),
    path('contents/<int:c_id>/<slug:c_slug>/',views.ContentDetailView.as_view(), name='home_detail_content'),


    path('dashboard/contents/', views.ContentDashboardListView.as_view(),
         name='dashboard_content_list'),
    path('dashboard/contents/create/', views.ContentDashboardCreateView.as_view(),
         name='dashboard_content_create'),
    path('dashboard/contents/<int:pk>/edit/',
         views.ContentDashboardUpdateView.as_view(), name='dashboard_content_edit'),
    path('dashboard/contents/<int:pk>/delete/',
         views.ContentDashboardDeleteView.as_view(), name='dashboard_content_delete'),

    path('dashboard/categories/', views.CategoryListView.as_view(),
         name='dashboard_category_list'),
    path('dashboard/categories/create/', views.CategoryCreateView.as_view(),
         name='dashboard_category_create'),
    path('dashboard/categories/<int:pk>/edit/',
         views.CategoryUpdateView.as_view(), name='dashboard_category_edit'),
    path('dashboard/categories/<int:pk>/delete/',
         views.CategoryDeleteView.as_view(), name='dashboard_category_delete'),

]
