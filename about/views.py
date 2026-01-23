from django.shortcuts import render
from .models import (
    AboutSection, 
    Branch, 
    CoreValue, 
    Leader, 
    StatementOfFaith, 
    BeliefPoint,
    HistoryMilestone,
    Statistic

)

def about_view(request):
    # 1. Fetch Single-Entry Data
    about_data = AboutSection.objects.first()
    sof_data = StatementOfFaith.objects.first()
    
    # 2. Fetch List Data (Ordered)
    core_values = CoreValue.objects.all().order_by('order')
    beliefs = BeliefPoint.objects.all().order_by('order')
    
    # 3. Fetch Related Data (Optimized)
    # prefetch_related handles the activities inside the branches
    branches = Branch.objects.filter(is_active=True).prefetch_related('activities')
    
    # select_related handles the branch name for each leader
    leaders = Leader.objects.all().select_related('branch').order_by('order')

    # 4. Debugging Logs (Check your terminal)
    if not about_data:
        print("!!! WARNING: No AboutSection data found !!!")
    if not sof_data:
        print("!!! WARNING: No StatementOfFaith data found !!!")

    # 5. Combine everything into the context
    context = {
        'about': about_data,
        'sof': sof_data,
        'core_values': core_values,
        'beliefs': beliefs,
        'branches': branches,
        'leaders': leaders,
        'history': HistoryMilestone.objects.all(),
        'stats': Statistic.objects.all(),
    }
    
    return render(request, 'about.html', context)



