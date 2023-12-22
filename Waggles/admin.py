from django.contrib import admin

# Register your models here.
from Waggles.models import *

# registering waggles
class WaggleLikeAdmin(admin.TabularInline):
    model = WaggleLike

class WaggleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['waggleText', 'user__username', 'user__email']
    class Meta:
        model = Waggle

admin.site.register(Waggle)
