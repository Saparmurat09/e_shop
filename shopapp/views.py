from rest_framework import generics
from rest_framework import permissions, authentication
from rest_framework_simplejwt.views import TokenObtainPairView


from .permissions import (
    # ProductCommentPermissions
    AdminPermissions
)

from .models import (
    User,
    Product,
    Address,
    Cart,
    # CartItem,
    Category,
    Comment,
    Order
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


class ListCreateAddress(generics.ListCreateAPIView):
    model = Address
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Address.objects.filter(user=user)


class ListCreateCart(generics.ListCreateAPIView):
    model = Cart
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Cart.objects.filter(user=user)


class ListCreateOrder(generics.ListCreateAPIView):
    model = Order

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Order.objects.filter(user=user)


class AddCartItem(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListCreateProduct(generics.ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(user=user)


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer


class ListCreateComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AdminPermissions]
    serializer_class = UserSerializer