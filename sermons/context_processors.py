from .models import AudioBroadcast


def active_broadcast(request):
    """
    Makes the currently live AudioBroadcast available in every template
    as {{ active_broadcast }}. Returns None if nothing is live.
    """
    broadcast = AudioBroadcast.objects.filter(is_live=True).first()
    return {
        'active_broadcast': broadcast,
    }
