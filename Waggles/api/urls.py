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
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", waggles_list_view),
    path("action/", waggle_action),
    path("create/", waggle_create_view),
    path("feed/", waggles_feed_view),
    path('?username=<str:username>/',  waggles_list_view),
    path("<int:waggle_id>/", waggle_detail_view),
    path("<int:waggle_id>/delete/", delete_waggle),
]
