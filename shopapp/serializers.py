from .models import (
                    User, Product, Address, Cart,
                    CartItem, Category, Comment, Order
                )

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.email
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(
                            write_only=True,
                            required=True,
                            validators=[validate_password]
                )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'is_admin',
            'is_staff',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            is_admin=validated_data['is_admin'],
            is_staff=validated_data['is_staff'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'is_admin',
            'is_staff',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'email',
            'name',
            'is_admin',
            'is_staff',
            'password',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'pictures',
            'category',
            'creation_date',
            'price',
            'quantity',
            'is_stock',
            'discount',
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'city',
            'microdistrict',
            'street',
            'flat_number',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'product',
            'replies',
            'rating',
            'creation_date',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'name',
            'total_price',
        ]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'cart',
            'product',
            'quantity',
            'price',
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'cart',
            'creation_date',
        ]
