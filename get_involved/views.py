from django.shortcuts import render
from .models import MembershipPathwayPage

def membership_pathway_view(request):
    # Get the singleton page config, or None if not set up yet
    page_config = MembershipPathwayPage.objects.first()
    
    context = {
        'page_config': page_config,
    }
    return render(request, 'membership_pathway.html', context)
