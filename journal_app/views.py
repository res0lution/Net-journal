from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm
from .models import Topic, Entry

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'journal_app/index.html')

@login_required
def topics(request):
    """Output topics lest"""
    ordered_topics = Topic.objects.filter(owner=request.user).order_by('date')
    context = {'topics': ordered_topics}
    return render(request, 'journal_app/topics.html', context)

@login_required
def topic(request, topic_id):
    """Output all entries of current topic"""
    current_topic = Topic.objects.get(id=topic_id)
    if current_topic.owner != request.user:
        raise Http404
    ordered_entries = current_topic.entry_set.order_by('-date')
    context = {'topic': current_topic, 'entries': ordered_entries}
    return render(request, 'journal_app/topic.html', context)

@login_required
def create_topic(request):
    """Define new topic"""
    if request.method != 'POST':
        """Empty form"""
        form = TopicForm()
    else:
        """Send data for new topic"""
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'journal_app/create_topic.html', context)

@login_required
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

@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Fill form via data from current entry
        form = EntryForm(instance=entry)
    else:
        #Send data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'journal_app/edit_entry.html', context)

def register(request):
    """Registration"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'journal_app/register.html', context)

        


    




