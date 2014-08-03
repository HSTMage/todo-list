from django.conf.urls import url

from todo_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
]