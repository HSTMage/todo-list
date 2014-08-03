from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tags(models.Model):
    tag  = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag

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