from django.db import models

# Create your models here.
class Item( models.Model):
    """items"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True)
    TYPE_STATUS = (
        ('type1', '1'),
        ('type2', '2'),
        ('type3', '3'),
        ('type4', '4'),
    )
    type = models.CharField(max_length=5,choices=TYPE_STATUS,blank=True,default='type1',
                            help_text= "Input type for item")
