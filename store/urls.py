from django.urls import path
from .views import register_user, create_cart, create_category, create_order, create_product, get_cart_items, get_category, get_orders, get_product, get_products, update_product, delete_product, add_to_cart
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    #AUTH
    path('register/', register_user),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    #PRODUCTS
    path('products/', get_products),
    path('products/<int:pk>/', get_product),
    path('product/create/', create_product),
    path('products/update/<int:pk>/', update_product),
    path('products/delete/<int:pk>/', delete_product),


    #CATEGORIES
    path('categories/', get_category),
    path('categories/create/', create_category),


    #CART
    path('cart/create/', create_cart),
    path('cart/add/', add_to_cart),
    path('cart/items/', get_cart_items),

    #ORDERS
    path('orders/create', create_order),
    path('orders/', get_orders)

]