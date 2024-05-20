from django import forms
from .models import Events, EventParticipation, EventComments

#use the QueryForm
class CreateNewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["name","date","description","country","city"]

class ParticipateAnEvent(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ["user","eventId","participation"]

class CreateEventComments(forms.ModelForm):
    class Meta:
        model = EventComments
        fields = ["user","eventId","text"]