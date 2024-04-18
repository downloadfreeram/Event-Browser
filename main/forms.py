from django import forms
from .models import Events

#use the QueryForm
class CreateNewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["name","date","description","country","city"]