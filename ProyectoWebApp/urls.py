from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]