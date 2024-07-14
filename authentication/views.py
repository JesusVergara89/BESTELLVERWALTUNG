from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class VRegister(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "authentication/authentication.html", {"form": form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "authentication/authentication.html", {"form": form})

def closeSession(request):
    logout(request)
    return redirect("home")

def login_session(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_ = form.cleaned_data.get("username")
            pass_=form.cleaned_data.get("password")
            user_ = authenticate(username=username_, password=pass_)
            if user_ is not None:
                login(request,user_)
                return redirect("home")
            else:
                messages.error(request, "not a valid user")
        else:
            messages.error(request, "Incorrect information")
            
    form=AuthenticationForm()
    return render(request, "login/login.html", {"form": form})