from django import contrib
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Item( models.Model):#akak product
    """items"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True)
    description  = models.CharField(max_length=200, default="this is the best drink")

    TYPE_STATUS = (
        ('favourite', 'favourite'),
        ('coffee', 'coffee'),
        ('fruit tea', 'fruit tea'),
        ('ICE BLENDED', 'ice blended'),
        ('snack', 'snack'),
    )
    type = models.CharField(max_length=11,choices=TYPE_STATUS,blank=True,default='favourite',
                            help_text= "Input type for item")
    def __str__(self):
        return self.name


class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    transaction_ID = models.CharField(max_length=100, null=True)
    complete = models.BooleanField(default=False, null=True)
   
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total=0
        for item in orderitems:
            total += item.get_total
        return total
    @property
    def get_cart_quantiy(self):
        orderitems = self.selforderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.address
