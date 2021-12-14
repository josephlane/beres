"""

    This Module contain test for Beres Application

"""
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Resource, Topic, Votes


class TopicModelTests(TestCase):
    """

    This test suite is responsible for encapsulating proper
    functionality for topics as they are utilized througout
    the program.

    Created by  : Joseph Lane
    Date        : 1/11/2018

    """

    def setUp(self):
        """

        This is boiler plate code that's needed for
        each subsequent test under topic

        """
        self.user = User.objects.create(
            username="abc123",
            password="abcd123",
            email="abcd123@123.com"
        )

    def test_create_with_name(self):
        """

        This test ensures a topic can be created with a name

        """
        topic_name = "Dynamic Programming"
        topic = Topic(
            name=topic_name,
            user=self.user
        )
        topic.save()
        self.assertEquals(topic.name == topic_name, True)


class ResourceModelTests(TestCase):
    """

    This test suite is responsible for encapsulating property
    functionality for resources that are mapped to topics.

    Created by    : Joseph Lane
    Date          : 1/11/2018

    """
    def setUp(self):
        """

        This is the boiler plate code that's needed for
        each subsequent test under Resource

        """
        self.user = User.objects.create(
            username="abc123",
            password="abcd123",
            email="abcd123@123.com"
        )
        self.topic = Topic(
            name="Stacks",
            user=self.user
        )
        self.topic.save()
        self.resource = Resource.objects.create(
            url="http://www.udemy.com",
            free=True,
            topic=self.topic,
            user=self.user
        )

    def test_create_free_resource(self):
        """

        This test ensures a resource can be created
        with a type set to free

        """
        self.assertEqual(self.resource.free, True)

    def test_create_paid_resource(self):
        """

        This test ensures a resource can be created
        with a type set to paid

        """
        resource = Resource.objects.get(pk=self.resource.id)
        resource.free = False
        resource.save()
        self.assertEqual(resource.free, False)

    def test_create_with_url(self):
        """

        This test ensures a resource can be created with
        URL

        """
        self.assertEqual(self.resource.url, "http://www.udemy.com")

    def test_resource_vote(self):
        """

        This test ensures a vote can be saved for resource

        """
        resource = Resource.objects.get(pk=self.resource.id)
        resource.save()
        Votes.objects.create(user=self.user, resource=resource, voted_up=True)
        vote = Votes.objects.filter(user=self.user).count()
        self.assertEqual(vote, 1)
