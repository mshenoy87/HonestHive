from django.conf import settings
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

from ..serializers import PublicProfileSerializer
from ..models import Profile
from ..serializers import PublicProfileSerializer

User = get_user_model()
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@api_view(['GET', 'POST'])
def profile_detail_api_view(request, username, *args, **kwargs):
    query_set = Profile.objects.filter(user__username=username)
    if not query_set.exists():
        return Response({"detail": "user not found"}, status=404)
    profile_object = query_set.first()
    data = request.data or {}
    # if we are trying to follow/unfollow, we are doing a post request
    if request.method == "POST":
        self_user = request.user
        action = data.get("action")
        # you cannot follow yourself - check if this is the case before proceeding
        if profile_object.user != self_user:
            if action == "follow":
                profile_object.followers.add(self_user)
            elif action == "unfollow":
                profile_object.followers.remove(self_user) 
            else:
                pass
    print("request: " + str(request))
    # get serialized profile contents and send it as a response
    serializer = PublicProfileSerializer(instance=profile_object, context={"request": request})
    return Response(serializer.data, status=200)

# @api_view(['GET'])
# def profile_detail_api_view(request, username, *args, **kwargs):
#     query_set = Profile.objects.filter(user__username=username)
#     # check if user exists in database. If not, raise error
#     if not query_set.exists():
#         return Response({"detail": "User not found"}, status=404)
#     profile_obj = query_set.first()
#     serializers = PublicProfileSerializer(instance=profile_obj, context={"request": request})
#     return Response(serializers.data, status=200)