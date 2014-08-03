from django.contrib import admin
from todo_app.models import Todo, Tags

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['todo', 'tags']}),
        ('Date information', {'fields': ['date_cre'], 'classes': ['collapse']}),
        ('Data', {'fields': ['author', 'deleted'], 'classes': ['collapse']}),
    ]
    
admin.site.register(Todo, TodoAdmin)
admin.site.register(Tags)
