from django.contrib import admin
from todo_app.models import Todo, Tags

class TodoAdmin(admin.ModelAdmin):
    fields = ['todo', 'author', 'date_cre']

admin.site.register(Todo)
admin.site.register(Tags)