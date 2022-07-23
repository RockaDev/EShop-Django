from django.contrib import admin
from pyparsing import Or

from shop.models import ShopItems,Customer,Order,OrderItem

# Register your models here.

admin.site.register(ShopItems)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)