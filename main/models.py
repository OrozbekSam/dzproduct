from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, related_name='user_product', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f'{self.title}'