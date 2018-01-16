from django.test import TestCase
from .models import Topic, Resource, Votes
from django.contrib.auth.models import User

class TopicModelTests(TestCase):
    """      
    This test suite is responsible for encapsulating proper functionality for topics as they are utilized througout the program.
    
    Created by  : Joseph Lane 
    Date        : 1/11/2018    
    """
    
    def setUp(self):
        self.user = User.objects.create(username="abc123", password="abcd123", email="abcd123@123.com")
    
    def test_created_with_name(self):
        topic_name = "Dynamic Programming"
        topic      = Topic(name=topic_name, user=self.user)
        topic.save()
        self.assertEquals(topic.name == topic_name, True)           

class ResourceModelTests(TestCase):
    """
    This test suite is responsible for encapsulating property functionality for resources that are mapped to topics.
    
    Created by    : Joseph Lane
    Date          : 1/11/2018
    
    """
    
    def setUp(self):
        self.user = User.objects.create(username="abc123", password="abcd123", email="abcd123@123.com")
        self.topic    = Topic(name="Stacks", user=self.user)
        self.topic.save()
        self.resource = Resource.objects.create(name="Udemy", url="www.udemy.com", free=True, topic=self.topic, user=self.user)
    
    def test_created_with_correct_name(self):
        self.assertEqual(self.resource.name == "Udemy", True)
        
    def test_created_with_type_set_to_free(self):
        self.assertEqual(self.resource.free, True)
        
    def test_created_with_type_set_to_paid(self):
        resource = Resource.objects.get(pk=self.resource.id)
        resource.free = False
        resource.save()
        self.assertEqual(resource.free, False)
        
    def test_created_with_url(self):
        self.assertEqual(self.resource.url, "www.udemy.com")
        
    def test_can_save_vote_on_resource(self):
        resource = Resource.objects.get(pk=self.resource.id)
        resource.save()
        Votes.objects.create(user=self.user, resource=resource)
        vote = Votes.objects.filter(user=self.user).count()
        self.assertEqual(vote, 1)
    
    