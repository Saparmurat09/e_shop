from .models import (
                    User, Product, Address, Cart,
                    CartItem, Category, Comment, Order
                )

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'phone_number',
            'name',
            'is_admin',
            'is_staff',
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
            'user',
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'city',
            'microdistrict',
            'street',
            'flat_number',
            'user',
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
            'user',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'name',
            'total_price',
            'user',
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
        fielsd = [
            'user',
            'cart',
        ]
