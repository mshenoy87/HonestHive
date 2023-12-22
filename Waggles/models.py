from django.db import models
from random import randint
from django.conf import settings
import pickle
from django.db.models import Q

##################################
# When changing the model run these commands in this order:
    # ./manage.py makemigrations
    # ./manage.py migrate
##################################

User = settings.AUTH_USER_MODEL

class WaggleLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waggle = models.ForeignKey("Waggle", on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)


class WaggleQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)
    
    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users = []
        if profiles_exist:
            followed_users = user.following.values_list("user__id", flat=True)
        return self.filter(
                Q(user__id__in=followed_users) |
                Q(user=user)
            ).distinct().order_by("-timestamp")


class WaggleManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return WaggleQuerySet(self.model, using=self.db)
    
    def feed(self, user):
        return self.get_queryset().feed(user)


# Create your models here.
class Waggle(models.Model):
    # id - Primary key
    # cascade makes it so that if user is deleted, all other waggles are deleted from that user
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can have many waggles
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL) # for retweet logic
    waggleText = models.TextField(blank=True, null=True)
    waggleImage = models.FileField(upload_to="images/", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='waggle_user', blank=True, through=WaggleLike)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = WaggleManager()

    # reverse the ordering (first waggle is bottom of screen)
    class Meta:
        ordering = ['-id']

    @property
    def is_rewaggle(self):
        # if waggle parent not returning None, then it is a rewaggle
        return self.parent != None

    