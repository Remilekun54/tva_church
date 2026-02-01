from django.urls import path
from . import views

urlpatterns = [
    path('membership/', views.membership_pathway_view, name='membership_pathway'),
    path('register/', views.registration_view, name='registration'),
]
