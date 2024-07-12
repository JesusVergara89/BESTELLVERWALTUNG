def total_basket(request):
    _total=0
    if request.user.is_authenticated:
        for key, value in request.session["basket"].items():
            _total = _total+(float(value["price"])*value["quantity"])
    return {"total_basket": _total}