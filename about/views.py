from django.shortcuts import render
from homepage.models import ChurchBranch
from .models import (
    AboutSection, 
    CoreValue, 
    Leader, 
    BeliefPoint,
    HistoryMilestone,
    Statistic,
    FoundingPastor,
    PresidingPastor,
    PastoralTeam
)

def about_view(request):
    # 1. Fetch Single-Entry Data
    about_data = AboutSection.objects.first()
    
    # 2. Fetch List Data (Ordered)
    core_values = CoreValue.objects.all().order_by('order')
    beliefs = BeliefPoint.objects.all().order_by('order')
    
    # 3. Fetch Related Data (Optimized)
    # prefetch_related handles the activities inside the branches
    branches = ChurchBranch.objects.all().order_by('order')
    
    # select_related handles the branch name for each leader
    leaders = Leader.objects.all().select_related('branch').order_by('order')

    # 4. Debugging Logs (Check your terminal)
    if not about_data:
        print("!!! WARNING: No AboutSection data found !!!")

    # 5. Combine everything into the context
    context = {
        'about': about_data,
        'core_values': core_values,
        'beliefs': beliefs,
        'branches': branches,
        'leaders': leaders,
        'history': HistoryMilestone.objects.all(),
        'stats': Statistic.objects.all(),
    }
    
    return render(request, 'about.html', context)

def founding_pastor_view(request):
    pastor_data = FoundingPastor.objects.first()
    
    context = {
        'pastor': pastor_data,
    }
    
    return render(request, 'founding_pastor.html', context)

def presiding_pastor_view(request):
    pastor_data = PresidingPastor.objects.first()
    
    context = {
        'pastor': pastor_data,
    }
    
    return render(request, 'presiding_pastor.html', context)

def pastoral_team_view(request):
    team_data = PastoralTeam.objects.first()
    
    context = {
        'team': team_data,
    }
    
    return render(request, 'pastoral_team.html', context)
