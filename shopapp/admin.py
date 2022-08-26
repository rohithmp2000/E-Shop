from django.contrib import admin

from .models import *

admin.site.register(Login)
admin.site.register(Seller)
admin.site.register(User)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)