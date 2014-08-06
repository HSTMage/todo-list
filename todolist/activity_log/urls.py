from django.conf.urls import url

from activity_log import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]