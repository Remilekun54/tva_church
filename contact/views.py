from django.shortcuts import render, redirect
from .models import ContactMessage, Branch # Import Branch
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, f"God bless you, {name}! Your message has been sent.")
        return redirect('contact')

    # Fetch all branches added by the admin
    branches = Branch.objects.all()
    
    return render(request, 'contact.html', {'branches': branches})