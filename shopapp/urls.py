from django.urls import path
from shopapp import views


urlpatterns = [
    path('', views.ListProduct.as_view(), name='products'),
    path('user/<int:pk>', views.RetrieveUser.as_view(), name='user'),
]