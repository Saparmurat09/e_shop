from django.urls import path
from shopapp import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)


urlpatterns = [
    path('products/', views.ListProduct.as_view(), name='products'),
    # path(
    #     'products/<int:pk>/',
    #     views.DetailProduct.as_view(),
    #     name='detail_product'
    # ),
    # path(
    #     'products/<int:pk>/comments/',
    #     views.ListCreateComment.as_view(),
    #     name='comments'
    # ),
    # path(
    #     'products/<int:pk>/comments/<int:comment>/replies/',
    #     views.ListCreateReply.as_view(),
    #     name='replies'
    # ),
    # path(
    #     'products/<int:pk>/add-to-cart/<int:cart>',
    #     views.CreateCartItem.as_view(),
    #     name='replies'
    # ),
    # path(
    #     'my-products/create/',
    #     views.CreateProduct.as_view(),
    #     name='create_product'
    # ),
    # path(
    #     'my-products/',
    #     views.ListCreateProduct.as_view(),
    #     name='my-products'
    # ),
    # path(
    #     'my-products/<int:pk>/',
    #     views.RetrieveProduct.as_view(),
    #     name='retrieve_product'
    # ),
    # path(
    #     'my-products/<int:pk>/comments/',
    #     views.ListComment.as_view(),
    #     name='retrieve_product'
    # ),
    # path(
    #     'cart/',
    #     views.ListCreateCart.as_view(),
    #     name='list_create_cart'
    # ),
    # path(
    #     'cart/<int:pk>',
    #     views.ListCartItem.as_view(),
    #     name='list_cart_item'
    # ),
    # path(
    #     'order/',
    #     views.ListCreateOrder.as_view(),
    #     name='list_create_order'
    # ),
    # path(
    #     'address/',
    #     views.ListCreateAddress.as_view(),
    #     name='list_create_address'
    # ),
    # path('category/', views.ListCreateCategory.as_view(), name='category'),

    # path(
    #     'login/',
    #     TokenObtainPairView.as_view(),
    #     name='token_obtain_pair'
    # ),
    # path(
    #     'login/refresh/',
    #     TokenRefreshView.as_view(),
    #     name='token_refresh'
    # ),
    # path('register/', views.RegisterView.as_view(), name='auth_register'),

    # path('users/', views.ListUser.as_view(), name='list_users'),
    # path('users/<int:pk>', views.DetailAdminUser.as_view(), name='admin_edit'),
    # path(
    #     'account/<str:pk>',
    #     views.AccountDetail.as_view(),
    #     name='account_detail'
    # ),
]
