from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from .models import User

# Create your tests here.


class TestHomePage(APITestCase):
    def test_homepage(self):

        url = reverse('products')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterLoginAuthTest(APITestCase):
    def test_register(self):
        url = reverse('register')

        data = {
            "email": "user@email.com",
            "name": "Userbek",
            "is_admin": False,
            "is_staff": False,
            "password": "Peasant12",
            "password2": "Peasant12"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):

        User.objects.create_user('user@email.com', 'Peasant12')

        data = {
            "email": "user@email.com",
            "password": "Peasant12"
        }

        url = reverse('login')

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())

    def test_auth(self):
        user = User.objects.create_user('user@email.com', 'Peasant12')

        data = {
            "email": "user@email.com",
            "password": "Peasant12"
        }

        url = reverse('login')

        response = self.client.post(url, data)

        access_token = response.json()['access']

        client = APIClient()

        client.force_authenticate(user, token=access_token)

        url = reverse('my-products')

        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
