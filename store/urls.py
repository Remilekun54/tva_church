from django.urls import path
from . import views

urlpatterns = [
    # The path should be empty if this is the app's 'home' page
    path('', views.store_view, name='store'), 
]