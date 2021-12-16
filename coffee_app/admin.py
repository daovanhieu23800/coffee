from django.contrib import admin
from coffee_app.models import Promotions
# Register your models here.
from coffee_app.models import Item, OrderItem, ShippingAddress,News
from coffee_app.models import Customer
from coffee_app.models import Order

admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(News)
admin.site.register(Promotions)