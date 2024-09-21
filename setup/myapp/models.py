from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Shop(models.Model):
    owner = models.ForeignKey(User, related_name="shops", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    shop = models.ForeignKey(Shop, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

