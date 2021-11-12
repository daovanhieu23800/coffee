from django.db import models

# Create your models here.

from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from users.models import Credit_card, account

class order(models.Model):
    id_order = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_order')
    ID_creditcard = models.ForeignKey(Credit_card,on_delete=models.DO_NOTHING)
    ID_user = models.ForeignKey(account,on_delete=models.CASCADE)
    address = models.CharField(max_length=30,null=False)
    payment_method = models.BooleanField() #true with card, false with cash
    accumulative_points = models.IntegerField(default=0,null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.id_order


class product(models.Model):
    url= models.FilePathField()
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False, verbose_name='ID_product')
    price = models.FloatField(null=False)
    Point = models.IntegerField(null=False)
    is_drink = models.BooleanField(null=False)
    def __str__(self):
        return self.id
    

class sub_order(models.Model):
    id_order = models.ForeignKey(order,on_delete=models.CASCADE)
    id_product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class drink(models.Model):
    class size(models.TextChoices):
        Small = 'S'
        Medium = 'L'
        BIg = 'XL'
    id_drink = models.ForeignKey(product,limit_choices_to={'is_drink':True},on_delete=models.CASCADE)
    name = models.CharField(max_length = 20, primary_key= True)
    sizeofdrink = models.CharField(max_length=2,choices=size.choices)
    topping = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class food (models.Model):
    id_food = models.ForeignKey(product,on_delete=models.CASCADE,limit_choices_to={'is_drink':False})
    name = models.CharField(max_length=20,primary_key=True)

class point:
    id_user = models.ForeignKey(account,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

class Promotion:
    id_promotion = models.AutoField(auto_created=True,primary_key=True,serialize=False, verbose_name='ID_promotion')
    id_user = models.ForeignKey(account,on_delete=models.CASCADE)
    Expirde_date = models.DateField()
    Number_of_point = models.IntegerField()
    Content = models.CharField(max_length = 200)