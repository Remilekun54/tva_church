from django.urls import path
from . import views

urlpatterns = [
    path('broadcast/status/', views.broadcast_status, name='broadcast_status'),
]