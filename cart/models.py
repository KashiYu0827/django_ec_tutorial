from django.db import models
from django.conf import setting
from mamazon.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_degits=9 ,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DataTimeField(auto_now=True)