from rest_framework import generics
from rest_framework import permissions, authentication
from rest_framework_simplejwt.views import TokenObtainPairView


from .permissions import (
    ProductCommentPermissions
)

from .models import (
    User,
    Product,
    # Address, Cart,
    # CartItem,
    Category,
    Comment,
    # Order
)

from .serializers import (
    RegistrationSerializer, CategorySerializer,
    ProductSerializer, AddressSerializer,
    CartSerializer, CartItemSerializer,
    CommentSerializer, OrderSerializer,
    CustomTokenObtainPairSerializer,
    UserSerializer,
)


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    serializer_class = RegistrationSerializer


class CreateAddress(generics.CreateAPIView):
    serializer_class = AddressSerializer


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateCart(generics.CreateAPIView):
    serializer_class = CartSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer


class AddCartItem(generics.CreateAPIView):
    serializer_class = CartItemSerializer


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer


class ListCreateComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
