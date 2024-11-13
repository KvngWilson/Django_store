from django.contrib import admin
from .models import Collection, User, Product, Order, ShippingAddress
# Register your models here.

admin.site.register(Collection)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShippingAddress)