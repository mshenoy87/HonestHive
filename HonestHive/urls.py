"""
URL configuration for HonestHive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from Waggles.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", home_page),
    path('admin/', admin.site.urls),
    path("login/", login_page),
    path("logout/", logout_page),
    re_path(r'profiles?/', include('profiles.urls')),
    path("register/", register_page),
    path('api/waggles/', include('Waggles.api.urls')),
    path('api/profiles/', include('profiles.api.urls')),
    path('react/', TemplateView.as_view(template_name='react.html')),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)