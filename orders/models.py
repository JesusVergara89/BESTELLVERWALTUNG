from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product
from django.db.models import F, Sum, FloatField

# Create your models here.
User=get_user_model()

class Orders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='orders'
        verbose_name='order'
        verbose_name_plural='orders'
        ordering=['id']
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.orders_lines_set.aggregate(
            total=Sum(F("price")*F("quantity"), output_field=FloatField)
        )["total"]

class orders_line(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order=models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    created_At = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} unidades de {}".format(self.quantity, self.product)
    
    class Meta:
        db_table='orders_lines'
        verbose_name='order_line'
        verbose_name_plural='orders_line'
        ordering=['id']