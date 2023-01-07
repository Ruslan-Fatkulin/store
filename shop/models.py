from django.contrib.auth.models import User
from .base_model import BaseModel
from django.db import models


class Product(BaseModel):
    name = models.CharField(max_length=255)
    preview = models.ImageField(blank=True)
    price = models.IntegerField()
    phone_number = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(blank=True)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

