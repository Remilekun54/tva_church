from django.shortcuts import render
from .models import Sermon, Book  # Import Book here
from about.models import Branch
from itertools import chain

def sermon_list(request):
    """View for the Media/Sermons page (Teachings)"""
    sermons = Sermon.objects.all().select_related('preacher', 'branch')
    branches = Branch.objects.all()

    branch_id = request.GET.get('branch')
    sort_type = request.GET.get('sort')

    if branch_id:
        sermons = sermons.filter(branch_id=branch_id)
    
    if sort_type == 'trending':
        sermons = sermons.filter(is_trending=True)
    else:
        sermons = sermons.order_by('-date_preached')

    context = {
        'sermons': sermons,
        'branches': branches,
        'current_branch': branch_id,
        'current_sort': sort_type,
    }
    return render(request, 'sermons.html', context)



from django.shortcuts import render
from .models import Sermon, Book 
from about.models import Branch
from itertools import chain

def store_view(request):
    # We use 'paid' (lowercase) because that is the value stored in your STATUS_CHOICES
    paid_sermons = Sermon.objects.filter(status='paid').select_related('preacher')
    paid_books = Book.objects.filter(status='paid')

    # Combine querysets into one list
    products = list(chain(paid_sermons, paid_books))

    # This print statement is for YOU to see in the terminal if it found anything
    print(f"DEBUG: Found {len(products)} paid items total.")

    context = {
        'products': products,
    }
    return render(request, 'store.html', context)