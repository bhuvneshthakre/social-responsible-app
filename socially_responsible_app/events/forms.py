from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date',)
        widgets = {
            'date': forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

