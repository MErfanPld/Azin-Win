"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls', namespace='content')),
    path('top/projects/', include('top_projects.urls', namespace='top_projects')),
    path('', include('order.urls', namespace='order')),
    path('about_us/', include('about_us.urls')),
    path('contact_us/', include('contact_us.urls', namespace='contact_us')),
]

urlpatterns += [
    path('api/auth/', include('accounts.api.urls')),
    path('api/sms/', include('sms.api.urls')),
    path('api/order/', include('order.api.urls')),
]

# if settings.DEBUG:
#     # add root static files
#     urlpatterns = urlpatterns + \
#                   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     # add media static files
#     urlpatterns = urlpatterns + \
#                   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
