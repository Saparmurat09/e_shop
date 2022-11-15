from django.urls import path
from shopapp import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)


urlpatterns = [
    path('', views.ListProduct.as_view(), name='products'),
    path('product', views.ListCreateProduct.as_view(), name='products'),
    path(
        'product/create',
        views.CreateProduct.as_view(),
        name='create_product'
    ),
    path(
        'cart/',
        views.ListCreateCart.as_view(),
        name='list_create_cart'
    ),
    path(
        'order/',
        views.ListCreateOrder.as_view(),
        name='list_create_order'
    ),
    path(
        'address/',
        views.ListCreateAddress.as_view(),
        name='list_create_address'
    ),

    path('category', views.ListCreateCategory.as_view(), name='category'),

    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'login/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('users/', views.ListUser.as_view(), name='list_users')
]
