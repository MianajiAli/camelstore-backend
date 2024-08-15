from rest_framework import generics
from .models import Category, Product, Cart, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer

# Category API views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product API views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Cart API views
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# CartItem API views
class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_pk = self.kwargs['cart_pk']
        return CartItem.objects.filter(cart_id=cart_pk)

    def perform_create(self, serializer):
        cart_pk = self.kwargs['cart_pk']
        cart = Cart.objects.get(pk=cart_pk)
        serializer.save(cart=cart)

class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_pk = self.kwargs['cart_pk']
        return CartItem.objects.filter(cart_id=cart_pk)
