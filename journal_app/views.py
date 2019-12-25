from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import forms
from .models import Topic

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'journal_app/index.html')

def topics(request):
    """Output topics lest"""
    ordered_topics = Topic.objects.order_by('date')
    context = {'topics': ordered_topics}
    return render(request, 'journal_app/topics.html', context)

def topic(request, topic_id):
    """Output all entries of current topic"""
    current_topic = Topic.objects.get(id=topic_id)
    ordered_entries = current_topic.entry_set.order_by('-date')
    context = {'topic': current_topic, 'entries': ordered_entries}
    return render(request, 'journal_app/topic.html', context)



