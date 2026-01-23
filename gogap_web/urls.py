from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from about.views import about_view
from homepage import views as home_views # Rename to avoid confusion
from sermons.views import sermon_list 
from events.views import event_list

# ADD THIS LINE: Import the store view from your store app
from store.views import store_view 
from events.views import event_list, register_event
# 1. Import your new contact view at the top
from contact.views import contact_view  

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_views.home, name='home'),
    path('about/', about_view, name='about'),
    path('sermons/', sermon_list, name='sermons'), 
    path('store/', store_view, name='store'),
    
    # 2. CHANGE THIS LINE to use contact_view instead of home_views.contact
    path('contact/', contact_view, name='contact'),
    
    path('offering/', home_views.offering, name='offering'),
    path('events/', event_list, name='events'),
    path('events/register/<int:event_id>/', register_event, name='register_event'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])