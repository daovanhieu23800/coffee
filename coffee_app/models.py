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

###promotion
class Promotions(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(null=False)
    content = models.CharField(max_length=80, default ="Discount 90%")
    expired = models.CharField(max_length=30, default="het han trong 2 ngay")
    discount = models.FloatField(default=0.1)

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    transaction_ID = models.CharField(max_length=100, null=True)
    complete = models.BooleanField(default=False, null=True)
    promotion = models.ForeignKey(Promotions,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total_before_promotion(self):
        orderitems = self.orderitem_set.all()
        total=0
        for item in orderitems:
            total += item.get_total
        ###check promotion
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total=0
        promo = self.promotion
        for item in orderitems:
            total += item.get_total
        ###check promotion
        if promo is None:
            print("null")
        else:
            total *= (1-promo.discount)
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
    size = models.CharField(max_length=1,default="S")
    note = models.CharField(max_length=50, default="normal")
    @property
    def get_total(self):
        plus = 0
        if self.size == 'M':
            plus = 5000
        elif self.size == 'L':
            plus = 10000
        total = self.item.price * self.quantity + plus*self.quantity
        return total
    @property
    def get_final_price(self):
        plus = 0
        if self.size == 'M':
            plus = 5000
        elif self.size == 'L':
            plus = 10000
        total = self.item.price + plus
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    instructions = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.address


###news 

class News(models.Model):
    title = models.CharField(max_length=100, null=False, default="title here")
    avatar = models.ImageField(null=False)
    content = models.CharField(max_length=300, default="pls input here")

    def __str__(self):
        return self.title





