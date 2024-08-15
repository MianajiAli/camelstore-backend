from django.urls import path
from . import views

urlpatterns = [
    # Category API endpoints
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Product API endpoints
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    # Cart API endpoints
    path('carts/', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', views.CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),

    # CartItem API endpoints
    path('carts/<int:cart_pk>/items/', views.CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('carts/<int:cart_pk>/items/<int:pk>/', views.CartItemRetrieveUpdateDestroyView.as_view(), name='cartitem-detail'),
]
    