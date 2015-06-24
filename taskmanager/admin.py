from django.contrib import admin

from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ['short_description','long_description','deadline','assigned_user']
    list_display = ['short_description','deadline','date_added','last_modified','assigned_user']

admin.site.register(Task,TaskAdmin)