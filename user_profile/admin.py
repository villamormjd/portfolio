from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name',)


admin.site.register(UserProfile, UserProfileAdmin)
