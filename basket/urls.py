from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="basket"

urlpatterns = [
    path('add/<int:product_id>', views.add_product, name='add_product'),
    path('delete/<int:product_id>', views.product_delete, name='product_delete'),
    path('substract/<int:product_id>', views.product_substract, name='product_substract'),
    path('clean/', views.basket_clean, name='basket_clean'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)