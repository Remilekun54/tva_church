
# Home Page View

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    HeroSlide, Sermon, Event, GalleryImage, 
    ContactMessage, FooterSettings, ChurchBranch
)

def home(request):
    # --- 1. HANDLE POST REQUESTS (Form Submissions) ---
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully! We will pray for you.")
        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            
        return redirect('home') 

    # --- 2. HANDLE GET REQUESTS (Page Loading) ---
    # Fetching data - using .filter(is_active=True) where applicable is safer
    slides = HeroSlide.objects.filter(is_active=True)
    latest_sermons = Sermon.objects.all().order_by('-id')[:4]
    events = Event.objects.all().order_by('id')[:4] 
    gallery_images = GalleryImage.objects.all()
    
    # Footer and Branch Data
    footer_settings = FooterSettings.objects.first()
    branches = ChurchBranch.objects.all()
    
    context = {
        'slides': slides,
        'sermons': latest_sermons,
        'events': events,
        'gallery_images': gallery_images,
        'footer': footer_settings,  # This name MUST match your HTML {{ footer... }}
        'branches': branches,
    }
    
    return render(request, 'index.html', context)



# About Page View
def about(request):
    return render(request, 'about.html')

# Sermons Page View
def sermons(request):
    return render(request, 'sermons.html')

# Store Page View
def store(request):
    return render(request, 'store.html')

3# Contact Page View
def contact(request):
    return render(request, 'contact.html')

# Offering Page View
def offering(request):
    return render(request, 'offering.html')

# Events Page View
def events(request):
    return render(request, 'events.html')



