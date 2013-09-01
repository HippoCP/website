from django.conf.urls import patterns, url

from wip import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
