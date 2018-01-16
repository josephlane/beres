from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

app_name = 'beres'

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/new', views.new_topic, name='new_topic'),
    path('<int:topic_id>/', views.detail, name='detail'),
    path('<int:topic_id>/new_resource/', views.new_resource, name='new_resource'),
    path('<int:topic_id>/save_resource/', views.save_resource, name='save_resource'),
    path('ajax/validate_topic_name/', views.validate_topic_name, name='validate_topic_name'),
    path('ajax/add_resource_vote/', views.add_resource_vote, name='add_resource_vote'),
    path('ajax/search_topic_name/', views.search_topic_name, name='search_topic_name'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page':'/beres'}, name='logout'),
    path('register/', views.register, name='register'),
]