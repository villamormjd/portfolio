from django.contrib import admin
from .models import Education


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'course', 'start_date')
    list_display_links = ('id', 'school')
    search_fields = ('school', 'course')


admin.site.register(Education, EducationAdmin)
