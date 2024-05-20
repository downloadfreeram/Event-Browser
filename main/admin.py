from django.contrib import admin
from .models import Events, EventParticipation, EventComments
# Register your models here.
admin.site.register(Events)
admin.site.register(EventParticipation)
admin.site.register(EventComments)

