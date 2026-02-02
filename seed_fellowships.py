import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gogap_web.settings')
django.setup()

from get_involved.models import Fellowship

fellowships = [
    ('BOX18', 'Box-18 (Men)'),
    ('VMUMS', 'V-Mums (Women)'),
    ('SINGLES', 'Singles & Youths'),
]

for name, title in fellowships:
    obj, created = Fellowship.objects.get_or_create(name=name, defaults={
        'about_text': f'Welcome to {title}. We are a community dedicated to growth and support.',
        'join_info': 'Join us at our next meeting!',
        'activities_summary': 'Weekly meetings, prayer sessions, and community outreach.',
    })
    if created:
        print(f"Created fellowship: {title}")
    else:
        print(f"Fellowship already exists: {title}")
