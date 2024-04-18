from django import forms
from .models import Events, EventParticipation

#use the QueryForm
class CreateNewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["name","date","description","country","city"]

class ParticipateAnEvent(forms.ModelForm):
    class MetaParticipate:
        model = EventParticipation
        fields = ["user","eventId","participation"]