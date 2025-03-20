from django import forms
from .models import Property, Appointment, Agent


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'image']

class AppointmentForm(forms.ModelForm):
    agent = forms.ModelChoiceField(queryset=Agent.objects.all(), required=False, empty_label="Select an Agent")

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'property', 'agent', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'email', 'phone', 'profile_picture']