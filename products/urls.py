from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('specific_products_dog/', views.specific_products_dog, name='specific_products_dog'),
    path('specific_products_cat/', views.specific_products_cat, name='specific_products_cat'),
    path('specific_products_bird/', views.specific_products_bird, name='specific_products_bird'),
    path('specific_products_dealz/', views.specific_products_dealz, name='specific_products_dealz'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
