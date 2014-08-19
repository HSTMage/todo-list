from django.contrib.auth.models import User
from django.db import models

class Tags(models.Model):
    tag  = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag
        
    def get_usage(self):
        return self.todo_set.all().count()
        
    get_usage.short_description = 'Vyuzitie'

class Todo(models.Model):
    todo = models.CharField(max_length=200)
    date_cre = models.DateTimeField('date created')
    deleted = models.CharField(max_length=1)
    author = models.ForeignKey(User) 
    tags = models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.todo
        
    def is_deleted(self):
        return self.deleted == '1'
      
    def get_author_name(self):
        _name = '%s' % (self.author.username)
        return _name.strip()
        
    get_author_name.short_description = 'Author'