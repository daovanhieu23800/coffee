from django.db import models

# Create your models here.
class Item( models.Model):
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