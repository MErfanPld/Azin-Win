from django.urls import path
from . import views

app_name = "faq"

urlpatterns = [
    path('', views.FAQListView.as_view(), name='faq_page'),
    path('dashboard/create', views.FAQCreateView.as_view(), name='create_faq'),
    path('dashboard/list', views.FAQDashboardList.as_view(), name='list_faq'),
    path('dashboard/edit/<int:pk>', views.FAQUpdateView.as_view(), name='update_faq'),
    path('dashboard/delete/<int:pk>', views.FAQDashboardDelete.as_view(), name='delete_faq'),

]
