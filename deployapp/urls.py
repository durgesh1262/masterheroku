from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Deployview, name = 'add'),
    
    
    
    
]
