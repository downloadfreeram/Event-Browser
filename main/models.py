from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#main database
class Events(models.Model):
    social = "SOCIAL"
    webinary = "WEBINARY"
    meeting = "MEETING"
    onlineMeeting = "ONLINE MEETING"
    other = "OTHER"
    choice = (
        (social,social),
        (webinary,webinary),
        (meeting,meeting),
        (onlineMeeting,onlineMeeting),
        (other,other)
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="event", 
        null=True)
    name = models.CharField(
        max_length=200
        ) 
    date = models.DateField()
    shortDescription = models.CharField(
        max_length=500
    )
    description = models.CharField(
        max_length = 2000)
    status = models.CharField(max_length=30,choices=choice,default=other)
    country = models.CharField(
        max_length = 25
        )
    city = models.CharField(
        max_length = 75
        )
    address = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.name

#additional database for users participation in an event
class EventParticipation(models.Model):
    user = models.CharField(
        max_length=100
        )
    eventId = models.IntegerField()
    name = models.CharField(
        max_length=200
    )
    date = models.DateField()
    participation = models.CharField(
        max_length=15
        )
    def __str__(self):
        return self.user

#additional database for comments in each event
class EventComments(models.Model):
    user = models.CharField(
        max_length=100,
        )
    eventId = models.IntegerField()
    commentData = models.DateTimeField(auto_now_add=True)
    text = models.CharField(
        max_length=1000
        )
    def __str__(self):
        return self.user