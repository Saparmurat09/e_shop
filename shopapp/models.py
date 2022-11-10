from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True

        user.is_admin = True

        user.save(using=self._db)


class User(AbstractBaseUser):
    email = models.EmailField(
            max_length=128,
            unique=True)

    phone_number = models.CharField()

    name = models.CharField(max_length=100, blank=False, null=False)

    is_admin = models.BooleanField(default=False, blank=True, null=False)
    is_staff = models.BooleanField(default=False, blank=True, null=False)

    USERNAME_FIELD = "email"

    objects = UserManager


class Address(models.Model):
    city = models.CharField(max_length=30, blank=False, null=False)
    microdistrict = models.CharField(max_length=30, blank=False, null=False)
    street = models.CharField(
            max_length=30,
            blank=False,
            null=False,
            help_text="Street name or Building number")
    flat_number = models.IntegerField(blank=False, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(
            max_length=20, blank=False,
            null=False, unique=True)


class Product(models.Model):

    title = models.CharField(
            max_length=100,
            blank=False,
            null=False,
            help_text="Title of the product")
    description = models.TextField(
                max_length=1000,
                blank=False,
                null=False,
                help_text="Description of a product")

    pictures = models.CharField(
            max_length=100,
            help_text="Link to image location")

    category = models.ForeignKey(
                Category,
                on_delete=models.DO_NOTHING,
                blank=True,
                null=True)

    creation_date = models.DateTimeField(auto_now=True, blank=False)

    price = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    is_stock = models.BooleanField(blank=False, null=False, default=True)

    discount = models.FloatField(blank=True, default=.0, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):

    content = models.CharField(max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    replies = models.ForeignKey("self", on_delete=models.CASCADE)

    ratings = [
        (1, "1")
        (2, "2")
        (3, "3")
        (4, "4")
        (5, "5")
    ]

    rating = models.IntegerField(choices=ratings)
    creation_date = models.DateTimeField(auto_now=True, blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    total_price = models.FloatField(blank=False, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
