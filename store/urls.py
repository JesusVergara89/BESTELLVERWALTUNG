from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.store, name='store'),
    path('categoriesproducts/<int:_id>/', views.categories_products, name='categoriesproducts'),
    path('singleproduct/<int:_id>/', views.single_product, name='singleproduct'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)