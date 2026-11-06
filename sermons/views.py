import os
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, FileResponse, Http404
from .models import Sermon, Book, SermonCategory, AudioBroadcast
from itertools import chain


def sermon_list(request):
    """View for the Media/Sermons page (Teachings)"""
    sermons = Sermon.objects.all().select_related('preacher', 'category')
    categories = SermonCategory.objects.all()
    
    # Get available years for filtering
    years = Sermon.objects.dates('date_preached', 'year', order='DESC')
    years = [date.year for date in years]

    category_slug = request.GET.get('category')
    year = request.GET.get('year')
    theme = request.GET.get('theme')
    sort_type = request.GET.get('sort')

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
        'categories': categories,
        'years': years,
        'current_category': category_slug,
        'current_year': year,
        'current_theme': theme,
        'current_sort': sort_type,
    }
    return render(request, 'sermons.html', context)


def download_sermon(request, sermon_id, media_type):
    """
    Forces immediate 1-click download of the sermon audio or video file to the user's gadget.
    """
    sermon = get_object_or_404(Sermon, pk=sermon_id)
    target_file = sermon.audio_file if media_type == 'audio' else sermon.video_file
    if not target_file:
        raise Http404("Media file is not available for this sermon.")
    
    try:
        file_path = target_file.path
        if not os.path.exists(file_path):
            raise Http404("File does not exist on server.")
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    except (ValueError, NotImplementedError):
        # Fallback for cloud storage backends where .path isn't local
        response = FileResponse(target_file.open('rb'), as_attachment=True)

    ext = os.path.splitext(target_file.name)[1]
    safe_title = "".join(c for c in sermon.title if c.isalnum() or c in (' ', '_', '-')).strip().replace(" ", "_")
    filename = f"{safe_title}_{media_type.capitalize()}{ext}"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


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


def radio_view(request):
    """
    View for the TVA Radio / Audio Archives page.
    Shows the current live broadcast (if any) and a list of all audio recordings.
    """
    # 1. Fetch live broadcast for the hero section
    current_live = AudioBroadcast.objects.filter(is_live=True).first()

    # 2. Fetch all sermons that have an uploaded audio file
    audio_sermons = Sermon.objects.exclude(
        audio_file=''
    ).exclude(audio_file__isnull=True).select_related('preacher').order_by('-date_preached')

    context = {
        'current_live': current_live,
        'audio_sermons': audio_sermons,
        'is_radio_page': True,
    }
    return render(request, 'radio.html', context)