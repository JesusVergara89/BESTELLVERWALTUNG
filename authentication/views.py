from django.shortcuts import render

# Create your views here.
def Authentication(request):
    return render(request, 'authentication/authentication.html')