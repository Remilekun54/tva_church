

from django.shortcuts import render
from .models import Event, EventCategory
from django.db.models import Q

def event_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    
    events = Event.objects.filter(is_active=True)
    categories = EventCategory.objects.all()

    if query:
        events = events.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        
    if category_id:
        events = events.filter(category_id=category_id)

    context = {
        'events': events,
        'categories': categories,
        'selected_category': category_id,
    }
    return render(request, 'events.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm



from django.contrib import messages # Import messages

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.event = event
            reg.save()
            
            # This line triggers the popup!
            messages.success(request, "Your spot has been reserved.")
            
            return redirect('register_event', event_id=event.id) 
    else:
        form = RegistrationForm()
    
    return render(request, 'events/register.html', {'form': form, 'event': event})