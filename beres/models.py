from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    name          = models.CharField(max_length=500, null=False, blank=False)
    created       = models.DateTimeField('date created', default=timezone.now)
    last_updated  = models.DateTimeField('last updated', default=timezone.now) 
    user          = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Resource(models.Model):
    name          = models.CharField(max_length=500)
    url           = models.CharField(max_length=500)
    topic         = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created       = models.DateTimeField('date created', default=timezone.now)
    last_updated  = models.DateTimeField('last updated', default=timezone.now)
    free          = models.BooleanField(null=False)
    user          = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    def total_resource_votes(self):
        total_positive_votes = Votes.objects.filter(resource_id=self.id, voted_up=True).count()
        total_negative_votes = Votes.objects.filter(resource_id=self.id, voted_up=False).count()
        return total_positive_votes - total_negative_votes
    
    def user_positive_vote(self):
        return Votes.objects.filter(user=self.user, resource_id=self.id, voted_up=True).count()
    
    def user_negative_vote(self):
         return Votes.objects.filter(user=self.user, resource_id=self.id, voted_up=False).count()   
    def user_voted(self):
        return Votes.objects.filter(user=self.user, resource_id=self.id,).count() > 0

class Votes(models.Model):
    resource      = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, on_delete=models.PROTECT)
    voted_up      = models.BooleanField(null=False)

		
