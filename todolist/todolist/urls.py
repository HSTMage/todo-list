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
    
    url(r'^$', views.index, name='index'),
    url(r'^doLogin/$', views.doLogin, name='doLogin'),
    url(r'^doLogout/$', views.doLogout, name='doLogout'),
    
    url(r'^register/$', views.register, name='register'),
    url(r'^doRegister/$', views.doRegister, name='doRegister'),
    
    url(r'^todo/', include('todo_app.urls', namespace="todo")),
    url(r'^activity/', include('activity_log.urls', namespace="activity")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

