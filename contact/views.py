from django.shortcuts import render, redirect
from .models import ContactMessage, Branch, Testimony, ContactPageSettings # Import new models
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'contact':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, f"God bless you, {name}! Your message has been sent.")
        
        elif form_type == 'testimony':
            name = request.POST.get('name')
            email = request.POST.get('email')
            testimony_content = request.POST.get('testimony_content')
            Testimony.objects.create(name=name, email=email, testimony_content=testimony_content)
            messages.success(request, f"Thank you, {name}! Your testimony has been shared to the glory of God.")
            
        return redirect('contact')

    # Fetch all branches added by the admin
    branches = Branch.objects.all()
    
    # Fetch settings
    settings = ContactPageSettings.objects.first()
    
    return render(request, 'contact.html', {'branches': branches, 'settings': settings})