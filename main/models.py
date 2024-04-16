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
    