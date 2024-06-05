from django import forms
from .models import Events, EventParticipation, EventComments

#use the QueryForm
class DateInput(forms.DateInput):
    input_type = "date"

class CreateNewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["name","date","shortDescription","description","status","country","city","address"]
        widgets = {
            'date':DateInput(),
            'status': forms.Select(attrs={"class": "form-control form-control-lg"}),
            'name': forms.TextInput(attrs={"class": "form-control form-control-lg"}),          
            'description': forms.Textarea(attrs={"class": "form-control"}), 
            'shortDescription': forms.Textarea(attrs={"class": "form-control"}), 
            'country': forms.TextInput(attrs={"class": "form-control form-control-lg"}), 
            'city': forms.TextInput(attrs={"class": "form-control form-control-lg"}), 
            'address': forms.TextInput(attrs={"class": "form-control form-control-lg"}), 
        }

class ParticipateAnEvent(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ["user","eventId","name","date","participation"]

class CreateEventComments(forms.ModelForm):
    class Meta:
        model = EventComments
        fields = ["user","eventId","text"]