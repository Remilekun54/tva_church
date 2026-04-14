from django.urls import path
from . import views

urlpatterns = [
    path('radio/', views.radio_view, name='radio'),
    path('broadcast/status/', views.broadcast_status, name='broadcast_status'),
]