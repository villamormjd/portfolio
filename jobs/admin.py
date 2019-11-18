from django.contrib import admin
from .models import Jobs


class JobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'hire_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'company')


admin.site.register(Jobs, JobsAdmin)
