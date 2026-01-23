from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        # Ensure these names match your ContactMessage model EXACTLY
        fields = ['name', 'email', 'message'] 
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'w-full bg-slate-100 border-none rounded-2xl p-5 outline-none font-bold text-primary',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'w-full bg-slate-100 border-none rounded-2xl p-5 outline-none font-bold text-primary',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message or prayer request...',
                'rows': 5,
                'class': 'w-full bg-slate-100 border-none rounded-2xl p-5 outline-none font-bold text-primary',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # This removes the default labels (Name:, Email:, etc.) 
        # so they don't clutter your design
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['message'].label = ""