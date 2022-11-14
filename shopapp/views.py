from rest_framework import generics
from .permissions import (
    ProductCommentPermissions
)

from .models import (
    User,
    Product,
    # Address, Cart,
    # CartItem, Category,
    Comment,
    # Order
)

from .serializers import (
    UserSerializer, CategorySerializer,
    ProductSerializer, AddressSerializer,
    CartSerializer, CartItemSerializer,
    CommentSerializer, OrderSerializer
)


class CreateAddress(generics.CreateAPIView):
    serializer_class = AddressSerializer


class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateCart(generics.CreateAPIView):
    serializer_class = CartSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer


class AddCartItem(generics.CreateAPIView):
    serializer_class = CartItemSerializer


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductCommentPermissions]


class ListCreateComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer