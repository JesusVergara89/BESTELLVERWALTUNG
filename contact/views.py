from django.shortcuts import render, redirect
from .form import Contact_form
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    form_contact=Contact_form()
    if request.method=='POST':
        form_contact=Contact_form(data=request.POST)
        if form_contact.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")
            new_content = "EL usuario {} \nCon email {}\nTe ha mandado el siguiente mensaje: {}\n\n".format(name,email,content)
            try:
                send_mail(name,new_content,'ingenierocivil.jmm@outlook.com',['jesusmanuelv1989@gmail.com'],fail_silently=False)
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?Fail_send")
            #print(name,email,content)            
    return render(request, 'contact/contact.html', {'Form_contac':form_contact })


