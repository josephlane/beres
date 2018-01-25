from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, Resource, Votes
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import TopicForm, CustomUserCreationForm, ResourceForm
from django.db.models import Count, F
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    """
    
    This function is responsible for capturing the trending topics and displaying them
    on the index page of the site
    
    """
    latest_topics = Topic.objects.all().annotate(resource_count=Count('resource')).order_by('-resource_count')[:10]
    topic_form = TopicForm()
    context = {'latest_topics': latest_topics, 'topic_form': topic_form}
    return render(request, 'beres/index.html', context)
    
def detail(request, topic_id):
    """
    
    This function is responsible for listing the Topic details.
    The detail will contain a listing of all of the corresponding resources
    
    """
    
    topic = get_object_or_404(Topic, pk=topic_id)
    
    user_votes_by_resource_id = []

    if request.user.is_authenticated:
        user_votes_by_resource_id = Votes.objects.filter(user=request.user).values_list('resource_id',
            flat=True)

    return render(request, 'beres/detail.html', {'topic': topic, 'user_votes':
        user_votes_by_resource_id})

def new_topic(request):
    """
    
    This function is responsible for creating a new topic
    
    """
    if request.user.is_authenticated:
        if request.method == "POST":   
            topic_form = TopicForm(request.POST)
            if topic_form.is_valid():
                name = request.POST['name']
                user = request.user
                topic = Topic(name=name, user=user)
                topic.save()
                return HttpResponseRedirect(reverse('beres:index'))
        else: 
            topic_form = TopicForm()
            return render(request, 'beres/new_topic.html', {'topic_form': topic_form})
    else:
         return HttpResponseRedirect(reverse('beres:index'))

def new_resource(request, topic_id):  
    """
    
    This function is responsible for rendering a new resource form
    
    """
    
    if request.user.is_authenticated:
        form = ResourceForm()
        context = {'topic_id': topic_id, 'form': form}
        return render(request, 'beres/new_resource.html', context)
    else:
        return HttpResponseRedirect(reverse('beres:index'))

def save_resource(request, topic_id):
    """
    
    This function is responsible for saving a new topic resource
    
    """
    if request.user.is_authenticated:
        topic        = get_object_or_404(Topic, pk=topic_id)
        form         = ResourceForm(request.POST)
        if form.is_valid():

            try:
                    url      = request.POST['url']
                    free     = True if request.POST['free'] == 'Free' else False
                    resource = Resource(topic=topic, url=url, free=free, user=request.user)
                    resource.save()
                    return HttpResponseRedirect(reverse('beres:detail', args=(topic.id,)))
            except Exception as e:
                return render(request, 'beres/new_resource.html', 
                             {'topic': topic, 'error_message': e})
        else:
            return render(request, 'beres/new_resource.html', {'topic': topic,
                'error_message': form.errors})
    else:
        return HttpResponseRedirect(reverse('beres:index'))

def validate_topic_name(request):   
    """
    
    This function determines whether the entered topic name is valid. It does
    this by searching for any pre-existing records that contain the same name
    
    """
    
    topic_name = request.GET.get('topic_name', None)
    data = {
        'is_taken': Topic.objects.filter(name__iexact=topic_name).exists()
    }
    
    if data['is_taken']:
        data['error_message'] = 'A topic with this name already exists.'
        
    return JsonResponse(data)

def add_resource_vote(request):
    """
    
    This function is responsible for adding user votes to a specified resource.
    A user can up-vote or down-vote a resource
    
    """
    if request.user.is_authenticated:
        
        resource_id         = request.GET.get('resource_id', None)  
        resource            = Resource.objects.get(pk=resource_id)
        vote_up             = True if request.GET.get('vote_up', None) == "true" else False
        existing_vote       = Votes.objects.filter(resource=resource, user=request.user)
        existing_vote_count = existing_vote.count()
        data = {}
        
        if existing_vote_count == 0:
            Votes.objects.create(resource=resource, user=request.user, voted_up=vote_up)

        elif existing_vote_count == 1:
            existing_vote.update(voted_up = vote_up)

            
        data['positive_votes'] = Votes.objects.filter(resource=resource, voted_up=True).count()
        data['negative_votes'] = Votes.objects.filter(resource=resource, voted_up=False).count()
        data['voted_up'] = vote_up == True

        return JsonResponse(data)



def search_topic_name(request):
    """
    
    This function takes the current text that is entered into search and queries the database for
    any hits
    
    """
    search_topic_name = request.GET.get('search_topic_name', None)
    topics = serializers.serialize("json",Topic.objects.filter(name__icontains=search_topic_name))

    data = {
        'topics': topics
    }
    return JsonResponse(data)

def contact_us(request):
    """
    
    This renders the contact us page
    
    """
    return render(request, 'beres/contact_us.html')

def about_us(request):
    """
    
    This renders the about us page
    
    """
    return render(request, 'beres/about_us.html')

def register(request):
    """
    
    This function is responsibile for registering new users
    
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/beres')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
