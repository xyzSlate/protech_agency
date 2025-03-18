from django import forms
from .models import Property, Appointment


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'image']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'property', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }