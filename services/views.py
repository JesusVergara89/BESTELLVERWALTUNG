from django.shortcuts import render
from services.models import services as serv

# Create your views here.

def services(request):
    services_=serv.objects.all()
    return render(request, 'services/services.html', {'services': services_})