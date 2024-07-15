from django.contrib import admin

# Register your models here.
from .models import Orders, orders_line

admin.site.register([Orders,orders_line])