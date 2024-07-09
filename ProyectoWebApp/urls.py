from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)