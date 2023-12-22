from rest_framework import serializers
from django.conf import settings
from profiles.serializers import PublicProfileSerializer
from .models import Waggle

MAX_WAGGLE_LENGTH = settings.MAX_WAGGLE_LENGTH
WAGGLE_ACTION_OPTIONS = settings.WAGGLE_ACTION_OPTIONS

class WaggleActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    waggleText = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()   # string formatting
        if not value in WAGGLE_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for waggles")
        return value


class WaggleCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = PublicProfileSerializer(source='user.profile', read_only=True)

    class Meta:
        model = Waggle
        fields = ["user", "id", "waggleText", "likes", "timestamp"]

    def get_likes(self, object):
        return object.likes.count()
    

    def validate_content(self, value):
        if (len(value) > MAX_WAGGLE_LENGTH):
            raise serializers.ValidationError("This waggle is too long!")
        return value


class WaggleSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    parent = WaggleCreateSerializer(read_only=True)
    
    class Meta:
        model = Waggle
        fields = [
                    "user",
                    "id",
                    "waggleText",
                    "likes",
                    "is_rewaggle",
                    "parent",
                    "timestamp"]

    def get_likes(self, object):
        return object.likes.count()
    