from django.shortcuts import render, HttpResponse

from basket.basket import basket as bas

# Create your views here.

def home(request):
    basket=bas(request)
    return render(request, 'ProyectoWebApp/home.html')

