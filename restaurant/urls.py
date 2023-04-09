from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.Menu, name='menu'),
    path('reservations', views.reservations, name='reservations'),
    path('gallery', views.gallery, name='gallery'),
    path('signup', views.handleSignup, name='handlesSignup'),
    path('login', views.handlelogin, name='handleslogin'),
    path('contacts', views.contacts, name='contact'),
]
