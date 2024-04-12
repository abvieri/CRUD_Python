from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=11)
    email = models.EmailField(max_length=254)
