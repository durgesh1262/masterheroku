from django.urls import path
from . import views

urlpatterns = [
    path('', views.Deployview),
    path('add/', views.Deployview, name = 'add'),
    
    
    
    
]
