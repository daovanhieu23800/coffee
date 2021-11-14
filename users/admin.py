from django.contrib import admin

from users.models import account,customer

# Register your models here.

admin.site.register(account)
admin.site.register(customer)