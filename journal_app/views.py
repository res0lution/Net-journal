from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
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

def create_topic(request):
    """Define new topic"""
    if request.method != 'POST':
        """Empty form"""
        form = TopicForm()
    else:
        """Send data for new topic"""
        form = TopicForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'journal_app/create_topic.html', context)

def create_entry(request, topic_id):
    """Add new entry to particular topic"""
    choosen_topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """Empty form"""
        form = EntryForm()
    else:
        """Send data for new topic"""
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = choosen_topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': choosen_topic, 'form': form}
    return render(request, 'journal_app/create_entry.html', context)


    




