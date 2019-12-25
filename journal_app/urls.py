"""Define url schems for net journal"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #Main page
    url(r'^topics/$', views.topics, name='topics'), #Topics page
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'), #Details topic page
    url(r'^new_topic/$', views.new_topic, name='new_topic'), #Topics page
]

