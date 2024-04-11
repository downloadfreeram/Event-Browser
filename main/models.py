from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=200)
    #type = models.
    date = models.DateField()
    description = models.CharField(max_length = 2000)
    country = models.CharField(max_length = 25)
    city = models.CharField(max_length = 75)

    def __str__(self):
        return self.name, self.date, self.description, self.country, self.city
    