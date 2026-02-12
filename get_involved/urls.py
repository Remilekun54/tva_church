from django.urls import path
from . import views

app_name = 'get_involved'

urlpatterns = [
    path('membership/', views.membership_pathway_view, name='membership_pathway'),
    path('register/', views.registration_view, name='registration'),
    path('city-altars/', views.city_altar_list_view, name='city_altar_list'),
    path('city-altars/<int:pk>/', views.city_altar_detail_view, name='city_altar_detail'),
    path('fellowships/<str:fellowship_type>/', views.fellowship_detail_view, name='fellowship_detail'),
    path('g12/', views.g12_view, name='g12_membership'),
]
