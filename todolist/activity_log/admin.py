from django.contrib import admin
from activity_log.models import ActivityLog

class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'get_author_name', 'date')
    list_filter = ['date']
    
admin.site.register(ActivityLog, ActivityLogAdmin)