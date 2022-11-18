from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .permissions import (
    StaffPermissions,
    AdminPermissions,
)

from .models import (
    User,
    Product,
    Address,
    Cart,
    CartItem,
    Category,
    Comment,
    Order
)

from .serializers import (
    RegistrationSerializer, CategorySerializer,
    CreateProductSerializer, AddressSerializer,
    CreateCartSerializer, ListCartSerializer,
    CreateCartItemSerializer, ListCartItemSerializer,
    OrderSerializer, UserSerializer,
    ListProductSerializer, UserDetailSerializer,
    CreateCommentSerializer, ListCommentSerializer,
)


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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, total_price=0.0)

    def get_queryset(self):
        user = self.request.user

        return Cart.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCartSerializer
        return ListCartSerializer


class ListCreateOrder(generics.ListCreateAPIView):
    model = Order

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Order.objects.filter(user=user)


class ListCreateProduct(generics.ListCreateAPIView):
    model = Product
    serializer_class = CreateProductSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListProductSerializer


class CreateProduct(generics.CreateAPIView):
    serializer_class = CreateProductSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveProduct(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = CreateProductSerializer

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(user=user)


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [StaffPermissions]
    serializer_class = CategorySerializer


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AdminPermissions]
    serializer_class = UserSerializer


class AccountDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()

    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.email != kwargs['pk']:
            return Response('No permission', status=403)

        serializer = UserDetailSerializer(user)

        return Response(serializer.data)


class DetailAdminUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    permission_classes = [AdminPermissions]
    serializer_class = UserDetailSerializer


class ListCreateComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated()]
    serializer_class = CreateCommentSerializer


class ListComment(generics.ListAPIView):
    queryset = Comment.objects.all()

    serializer_class = ListCommentSerializer

    def get_queryset(self):
        product = self.kwargs['pk']

        return Comment.objects.filter(product=product)


class ListCreateComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()

    def get_queryset(self):
        product = self.kwargs['pk']
        return Comment.objects.filter(product=product)

    def perform_create(self, serializer):
        product = self.kwargs['pk']
        serializer.save(
            user=self.request.user,
            product=Product.objects.get(id=product)
        )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCommentSerializer
        return ListCommentSerializer


class ListCreateReply(generics.ListCreateAPIView):
    queryset = Comment.objects.all()

    def get_queryset(self):
        product = self.kwargs['pk']
        comment = self.kwargs['comment']
        return Comment.objects.filter(product=product, replies=comment)

    def perform_create(self, serializer):
        product = self.kwargs['pk']
        comment = self.kwargs['comment']
        serializer.save(
            user=self.request.user,
            product=Product.objects.get(id=product),
            replies=Comment.objects.get(id=comment)
        )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCommentSerializer
        return ListCommentSerializer


class ListCartItem(generics.ListAPIView):
    queryset = CartItem.objects.all()

    serializer_class = ListCartItemSerializer

    def get_queryset(self):
        cart = self.kwargs['pk']

        return CartItem.objects.filter(cart=cart)


class CreateCartItem(generics.CreateAPIView):
    serializer_class = CreateCartItemSerializer

    def perform_create(self, serializer):
        product = self.kwargs['pk']
        product = Product.objects.get(id=product)
        cart = self.kwargs['cart']
        cart = Cart.objects.get(id=cart)
        quantity = serializer.validated_data['quantity']

        print(cart.total_price)

        price = product.price * quantity

        product.quantity = (product.quantity - quantity)
        cart.total_price = (cart.total_price + price)

        product.save()
        cart.save()

        print(cart.total_price)

        serializer.save(
            cart=cart,
            product=product,
            price=price,
        )
