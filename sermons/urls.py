
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sermon_list, name='sermons'), 
    path('store/', views.store_view, name='store'), # ADD THIS LINE
]