from django.conf.urls import url

from todo_app import views

urlpatterns = [
    url(r'^list$', views.todo_list, name='todo_list'),
]