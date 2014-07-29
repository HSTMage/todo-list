from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=200)
    date_cre = models.DateTimeField('date created')
    deleted = models.CharField(max_length=1)
    author = models.ForeignKey(User) 
    
    def __str__(self):
        return self.todo
    
class Tags(models.Model):
    todo = models.ForeignKey(Todo)
    tag  = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag