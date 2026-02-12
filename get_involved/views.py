from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MembershipPathwayPage, CityAltar, Fellowship, FellowshipEvent
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ChurchMembershipForm, DepartmentRegistrationForm

def membership_pathway_view(request):
    # Get the singleton page config, or None if not set up yet
    page_config = MembershipPathwayPage.objects.first()
    
    context = {
        'page_config': page_config,
    }
    return render(request, 'membership_pathway.html', context)

def registration_view(request):
    membership_form = ChurchMembershipForm(prefix='member')
    department_form = DepartmentRegistrationForm(prefix='dept')

    if request.method == 'POST':
        if 'submit_member' in request.POST:
            membership_form = ChurchMembershipForm(request.POST, prefix='member')
            if membership_form.is_valid():
                membership_form.save()
                messages.success(request, 'Welcome to the family! Your membership registration has been received.')
                return redirect('registration')
        elif 'submit_dept' in request.POST:
            department_form = DepartmentRegistrationForm(request.POST, prefix='dept')
            if department_form.is_valid():
                department_form.save()
                messages.success(request, 'Thank you for volunteering! The department lead will contact you soon.')
                return redirect('registration')

    context = {
        'membership_form': membership_form,
        'department_form': department_form,
    }
    return render(request, 'registration.html', context)

def city_altar_list_view(request):
    """View to list all City Altars (House Fellowships)"""
    altars = CityAltar.objects.all().order_by('location', 'name')
    context = {
        'altars': altars,
    }
    return render(request, 'city_altar_list.html', context)

def city_altar_detail_view(request, pk):
    """View to show details of a specific City Altar"""
    altar = get_object_or_404(CityAltar, pk=pk)
    context = {
        'altar': altar,
    }
    return render(request, 'city_altar_detail.html', context)

def fellowship_detail_view(request, fellowship_type):
    """View to show details of a specific fellowship (Box-18, V-Mums, Singles)"""
    # map url slug to model choices
    type_map = {
        'box-18': 'BOX18',
        'v-mums': 'VMUMS',
        'singles-youths': 'SINGLES'
    }
    
    db_type = type_map.get(fellowship_type)
    if not db_type:
        return redirect('home') # or 404
        
    fellowship = get_object_or_404(Fellowship, name=db_type)
    
    # Split events
    now = timezone.now().date()
    future_events = fellowship.events.filter(date__gte=now).order_by('date')
    past_events = fellowship.events.filter(date__lt=now).order_by('-date')
    
    context = {
        'fellowship': fellowship,
        'future_events': future_events,
        'past_events': past_events,
    }
    return render(request, 'fellowship_detail.html', context)

from .models import G12Page
from .forms import G12RegistrationForm

def g12_view(request):
    page_data = G12Page.objects.first()
    form = G12RegistrationForm()
    
    if request.method == 'POST':
        form = G12RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration for the G-12 class has been received successfully!')
            return redirect('get_involved:g12_membership')
            
    context = {
        'page': page_data,
        'form': form,
    }
    return render(request, 'g12.html', context)
