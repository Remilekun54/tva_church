from django.urls import path
from . import views

urlpatterns = [
    path('radio/', views.radio_view, name='radio'),
    path('download/<int:sermon_id>/<str:media_type>/', views.download_sermon, name='sermon_download_app'),
    path('broadcast/status/', views.broadcast_status, name='broadcast_status'),
]