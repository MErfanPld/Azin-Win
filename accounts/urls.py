from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings

# app_name = "accounts"

urlpatterns = [
    path('dashboard/user/list', UserDashboardList.as_view(), name='list_user'),
    path('dashboard/user/create', UserCreateView.as_view(), name='create_user'),
    path('dashboard/user/edit/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('dashboard/user/delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyCodeView.as_view(), name='verify-code'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),

    path('password/reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('password/reset/confirm/', VerifyCodeView.as_view(), name='password-reset-confirm'),
    path('password/reset/enter/', ResetPasswordEnterView.as_view(), name='password-reset-enter'),
]
