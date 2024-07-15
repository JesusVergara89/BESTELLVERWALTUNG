from django.urls import path

from .views import VRegister, closeSession, login_session

urlpatterns = [
    path('', VRegister.as_view(), name='authentication'),
    path('closesession', closeSession, name='closesession'),
    path('loggear', login_session, name='loggear'),
]

