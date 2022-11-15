from django.urls import path
from shopapp import views

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.ListProduct.as_view(), name='products'),
    path('user/<int:pk>', views.RetrieveUser.as_view(), name='user'),
    path(
        'product/create',
        views.CreateProduct.as_view(),
        name='create_product'
    ),

    path('category', views.ListCreateCategory.as_view(), name='category'),

    path(
        'login/',
        views.CustomObtainTokenPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'login/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]
