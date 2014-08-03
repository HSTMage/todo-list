from django.conf.urls import patterns, include, url

from rest_framework import routers
from todolist import views
from todo_app import urls

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
#router.register(r'todo', views.TodoListView)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^$', views.index, name='index'),
    url(r'^', include('todo_app.urls'), namespace="todos"),
    url(r'^todo/', include('todo_app.urls'), namespace="todos"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)