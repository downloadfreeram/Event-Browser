from django import forms
from .models import Events, EventParticipation, EventComments

#use the QueryForm
class DateInput(forms.DateInput):
    input_type = "date"

class CreateNewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["name","date","description","country","city"]
        widgets = {
            'date':DateInput(),
        }

class ParticipateAnEvent(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ["user","eventId","participation"]

class CreateEventComments(forms.ModelForm):
    class Meta:
        model = EventComments
        fields = ["user","eventId","text"]