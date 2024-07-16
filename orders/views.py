from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from basket.basket import basket
from orders.models import Orders, orders_line
from django.contrib import messages

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
            nameUser=request.username,
            email_user=request.usermail
    )

    messages.success(request, "The order have been created succesfylly")

    return redirect("../store")


def send_order(**kwargs):
    pass
