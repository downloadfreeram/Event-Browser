from django.contrib import admin
from .models import Events, EventParticipation
# Register your models here.
admin.site.register(Events)
admin.site.register(EventParticipation)

