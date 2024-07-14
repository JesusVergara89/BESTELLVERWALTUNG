from django.urls import path

from .views import VRegister, closeSession

urlpatterns = [
    path('', VRegister.as_view(), name='Authentication'),
    path('closesession', closeSession, name='closesession'),
]

