"""Define url schems for net journal"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #Main page
    url(r'^topics/$', views.topics, name='topics'), #Topics page
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'), #Details topic page
    url(r'^create_topic/$', views.create_topic, name='create_topic'), #Create topic page
    url(r'^create_entry/(?P<topic_id>\d+)/$', views.create_entry, name='create_entry'), #Create entry page
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'), #Edit entry page
    url(r'^register/$', views.register, name='register'),
]

