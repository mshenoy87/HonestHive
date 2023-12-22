from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from ..models import Waggle
from ..serializers import WaggleSerializer, WaggleActionSerializer, WaggleCreateSerializer
from ..forms import WaggleForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
@api_view(['POST'])   # always equals POST
@permission_classes([IsAuthenticated])
def waggle_create_view(request, *args, **kwargs):
   # send the data we recieve in the request to WaggleCreateSerializer
   serializer = WaggleCreateSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=201)
   return Response({}, status=400)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def delete_waggle(request, waggle_id, *args, **kwargs):
   query_set = Waggle.objects.filter(id=waggle_id)
   if not query_set.exists():
      return Response({}, status=404)
   query_set = query_set.filter(user=request.user)
   if not query_set.exists():
      return Response({"message": "You cannot delete this waggle"}, status=401)
   obj = query_set.first()
   obj.delete()
   return Response({"message": "Waggle removed"}, status=200)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def waggle_action(request, *args, **kwargs):
   '''
   actions: like, unlike, re-waggle
   '''
   # get serializer data from serializers.py
   serializer = WaggleActionSerializer(data=request.data)
   if serializer.is_valid(raise_exception=True):
      data = serializer.validated_data
      waggle_id = data.get("id")
      action = data.get("action")
      waggleText = data.get("waggleText")
   query_set = Waggle.objects.filter(id=waggle_id)

   if not query_set.exists():
      return Response({}, status=404)
   obj = query_set.first()

   # handle like, unlike, and rewaggle 
   # probably a better way to do this in case we want to incorporate more actions but that is a case for later
   if action == "like":
      obj.likes.add(request.user)
      serializer = WaggleSerializer(obj)
      return Response(serializer.data, status=200)
   elif action == "unlike":
      obj.likes.remove(request.user)
   elif action == "rewaggle":
      new_waggle = Waggle.objects.create(user=request.user, parent=obj, waggleText=obj.waggleText)
      serializer = WaggleSerializer(new_waggle)
      return Response(serializer.data, status=200)
   return Response({}, status=200)

def get_paginated_queryset_response(qs, request):
   paginator = PageNumberPagination()
   paginator.page_size = 5
   paginated_qs = paginator.paginate_queryset(qs, request)
   serializer = WaggleSerializer(paginated_qs, many=True, context={"request": request})
   return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def waggles_list_view(request, *args, **kwargs):
   query_set = Waggle.objects.all()
   username = request.GET.get('username')  
   if username != None:
      query_set = query_set.by_username(username)
   # return get_paginated_queryset_response(query_set, request)
   serializer = WaggleSerializer(query_set, many=True, context={"request": request})
   return get_paginated_queryset_response(query_set, request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def waggles_feed_view(request, *args, **kwargs):
   user = request.user
   qs = Waggle.objects.feed(user)
   return get_paginated_queryset_response(qs, request)

@api_view(['GET'])
def waggle_detail_view(request, waggle_id, *args, **kwargs):
    qs = Waggle.objects.filter(id=waggle_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = WaggleSerializer(obj)
    return Response(serializer.data, status=200)

