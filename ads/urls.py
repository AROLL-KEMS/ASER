from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='test'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    
]


