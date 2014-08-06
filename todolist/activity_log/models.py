from django.contrib.auth.models import User
from django.db import models

class ActivityLog(models.Model):
    action = models.CharField(max_length=200)
    date = models.DateTimeField('date created')
    author = models.ForeignKey(User) 
        
    def __str__(self):
        return self.action
      
    def get_author_name(self):
        _name = '%s' % (self.author.username)
        return _name.strip()
        
    get_author_name.short_description = 'Author'