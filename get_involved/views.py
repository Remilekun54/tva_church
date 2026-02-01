from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MembershipPathwayPage
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
