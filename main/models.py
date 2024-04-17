from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Events(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="event", 
        null=True)
    name = models.CharField(
        max_length=200
        )
    date = models.DateField(
        default = timezone.now
        )
    description = models.CharField(
        max_length = 2000)
    country = models.CharField(
        max_length = 25
        )
    city = models.CharField(
        max_length = 75
        )

    def __str__(self):
        return self.name

# class EventParticipation(models.Models):
#     class Options(models.TextChoices):
#         will = "yes"
#         willnot = "no"
#     user = models.ForeignKey(Events.user, on_delete=models.CASCADE,related_name="eventParticipation",null=True)
#     event = models.ForeignKey(Events.id)
#     participation = models.CharField(max_length=3,choices=Options,default=Options.willnot)
#     def __str__(self):
#         return self.name
    