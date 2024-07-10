from django.shortcuts import render, redirect
from .form import Contact_form

# Create your views here.
def contact(request):
    form_contact=Contact_form()
    if request.method=='POST':
        form_contact=Contact_form(data=request.POST)
        if form_contact.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")
            #print(name,email,content)
            return redirect("/contact/?valid")
    return render(request, 'contact/contact.html', {'Form_contac':form_contact })


