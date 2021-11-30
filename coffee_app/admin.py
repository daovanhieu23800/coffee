from django.contrib import admin
# Register your models here.
from coffee_app.models import Item, OrderItem, ShippingAddress
from coffee_app.models import Customer
from coffee_app.models import Order

admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)