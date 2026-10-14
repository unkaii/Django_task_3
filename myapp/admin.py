from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date', 'created_at')
    list_filter = ('subject', 'grade')
    search_fields = ('student', 'subject')
    date_hierarchy = 'date'