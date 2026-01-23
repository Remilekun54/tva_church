from django import forms
from .models import EventRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['full_name', 'email', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full p-4 rounded-2xl border border-slate-200', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-4 rounded-2xl border border-slate-200', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full p-4 rounded-2xl border border-slate-200', 'placeholder': 'Phone Number'}),
        }