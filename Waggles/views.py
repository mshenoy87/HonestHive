from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .serializers import WaggleSerializer, WaggleActionSerializer, WaggleCreateSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Waggle
from Waggles.forms import WaggleForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_page(request, *args, **kwargs):
   # What you should see when you come to the home page
   return render(request, template_name="pages/feed.html")

def waggle_detail_view(request, waggle_id, *args, **kwargs):
   pass
