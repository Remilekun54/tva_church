from django import forms
from .models import ChurchMembershipRegistration, DepartmentRegistration

class ChurchMembershipForm(forms.ModelForm):
    class Meta:
        model = ChurchMembershipRegistration
        fields = ['full_name', 'email', 'phone_number', 'address', 'date_of_birth', 'gender', 'how_did_you_hear']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none', 'rows': 3, 'placeholder': 'Home Address'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none'}),
            'gender': forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none bg-white'}),
            'how_did_you_hear': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 transition-all outline-none', 'placeholder': 'Friend, Social Media, etc.'}),
        }

class DepartmentRegistrationForm(forms.ModelForm):
    class Meta:
        model = DepartmentRegistration
        fields = ['full_name', 'email', 'phone_number', 'department', 'reason_for_joining']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-secondary focus:ring-4 focus:ring-secondary/10 transition-all outline-none', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-secondary focus:ring-4 focus:ring-secondary/10 transition-all outline-none', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-secondary focus:ring-4 focus:ring-secondary/10 transition-all outline-none', 'placeholder': 'Phone Number'}),
            'department': forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-secondary focus:ring-4 focus:ring-secondary/10 transition-all outline-none bg-white'}),
            'reason_for_joining': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-secondary focus:ring-4 focus:ring-secondary/10 transition-all outline-none', 'rows': 3, 'placeholder': 'Tell us why you want to serve...'}),
        }
