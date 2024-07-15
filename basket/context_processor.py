def total_basket(request):
    total = 0
    if request.user.is_authenticated:
        if 'basket' in request.session:
            for key, value in request.session["basket"].items():
                total = total+float(value["price"])
    return {"total_basket": total}