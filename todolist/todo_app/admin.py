from django.contrib import admin
from todo_app.models import Todo, Tags

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['todo', 'tags']}),
        ('Date information', {'fields': ['date_cre'], 'classes': ['collapse']}),
        ('Data', {'fields': ['author', 'deleted'], 'classes': ['collapse']}),
    ]
    list_display = ('todo', 'get_author_name', 'date_cre')
    list_filter = ['date_cre']
    search_fields = ['todo']
    
admin.site.register(Todo, TodoAdmin)
admin.site.register(Tags)
