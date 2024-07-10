from django.shortcuts import render
from .form import Contact_form

# Create your views here.
def contact(request):
    form_contact=Contact_form()
    return render(request, 'contact/contact.html', {'Form_contac':form_contact })


