from django.db import models

# Create your models here.
class Item( models.Model):
    """items"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True)