from django.shortcuts import render
from django.http import JsonResponse
from .models import Sermon, Book, SermonCategory, AudioBroadcast
from about.models import Branch
from itertools import chain


def sermon_list(request):
    """View for the Media/Sermons page (Teachings)"""
    sermons = Sermon.objects.all().select_related('preacher', 'branch', 'category')
    branches = Branch.objects.all()
    categories = SermonCategory.objects.all()
    
    # Get available years for filtering
    years = Sermon.objects.dates('date_preached', 'year', order='DESC')
    years = [date.year for date in years]

    branch_id = request.GET.get('branch')
    category_slug = request.GET.get('category')
    year = request.GET.get('year')
    theme = request.GET.get('theme')
    sort_type = request.GET.get('sort')

    if branch_id:
        sermons = sermons.filter(branch_id=branch_id)
    
    if category_slug:
        sermons = sermons.filter(category__slug=category_slug)
    
    if year:
        sermons = sermons.filter(date_preached__year=year)
        
    if theme:
        sermons = sermons.filter(theme__icontains=theme)
    
    if sort_type == 'trending':
        sermons = sermons.filter(is_trending=True)
    else:
        sermons = sermons.order_by('-date_preached')

    context = {
        'sermons': sermons,
        'branches': branches,
        'categories': categories,
        'years': years,
        'current_branch': branch_id,
        'current_category': category_slug,
        'current_year': year,
        'current_theme': theme,
        'current_sort': sort_type,
    }
    return render(request, 'sermons.html', context)


def broadcast_status(request):
    """
    JSON API endpoint polled by the frontend player.
    Returns the current live broadcast state so the JS player
    can update without a full page reload.
    """
    broadcast = AudioBroadcast.objects.filter(is_live=True).first()
    if broadcast:
        return JsonResponse({
            'is_live': True,
            'title': broadcast.title,
            'preacher': broadcast.preacher.name if broadcast.preacher else '',
            'hls_url': broadcast.hls_stream_url,
        })
    return JsonResponse({'is_live': False})


def store_view(request):
    # We use 'paid' (lowercase) because that is the value stored in your STATUS_CHOICES
    paid_sermons = Sermon.objects.filter(status='paid').select_related('preacher')
    paid_books = Book.objects.filter(status='paid')

    # Combine querysets into one list
    products = list(chain(paid_sermons, paid_books))

    print(f"DEBUG: Found {len(products)} paid items total.")

    context = {
        'products': products,
    }
    return render(request, 'store.html', context)