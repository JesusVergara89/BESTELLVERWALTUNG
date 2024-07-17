from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from basket.basket import basket
from orders.models import Orders, orders_line
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail 

# Create your views here.
@login_required(login_url="/authentication/login")
def process_order(request):
    order_=Orders.objects.create(user=request.user)
    _basket=basket(request)
    list_order=list()
    for key, value in _basket.basket_.items():
        list_order.append(orders_line(
            product_id=key,
            quantity=value["quantity"],
            user=request.user,
            order=order_
        ))

    
    orders_line.objects.bulk_create(list_order)

    send_order(
            order=order_,
            list_order=list_order,
            nameUser=request.user.username,
            email_user=request.user.email
    )

    messages.success(request, "The order have been created succesfylly")

    return redirect("../store")


def send_order(**kwargs):
    subject="Thank you for the order"
    msj=render_to_string("email/store_order.html",{
        "order": kwargs.get("order"),
        "list_order": kwargs.get("list_order"),
        "nameUser": kwargs.get("nameUser")
    })
    msj_txt=strip_tags(msj)
    from_email="ingenierocivil.jmm@outlook.com"
    #to_=kwargs.get("email_user")
    to_="jesusmanuelitsa1989@gmail.com"

    send_mail(subject,msj_txt, from_email,[to_],html_message=msj)


