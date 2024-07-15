class basket:

    def __init__(self, request):
        self.request=request
        self.session=request.session
        basket_=self.session.get("basket")
        if not basket_:
            basket_ = self.session["basket"] = {}
        self.basket_ = basket_

    def add(self, product):
        if (str(product.id) not in self.basket_.keys()):
            self.basket_[product.id]={
                "product_id": product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "image": product.image.url
            }
        else:
            for key, value in self.basket_.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    value["price"] = float(value["price"]) + product.price
                    break
        self.save_basket()
    
    def save_basket(self):
        self.session["basket"] = self.basket_
        self.session.modified = True
    
    def delete_product(self, product):
        product_id = str(product.id)
        if product_id in self.basket_:
            del self.basket_[product_id]
            self.save_basket()
    
    def substract_product(self, product):
        for key, value in self.basket_.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                value["price"] = float(value["price"]) - product.price
                if value["quantity"] < 1:
                    self.delete_product(product)
                    break
        self.save_basket()
    
    def clean_basket(self):
        self.session["basket"] = {}
        self.session.modified = True