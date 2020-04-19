from django.apps import AppConfig
from .models import Order, OrderLineItem
from django.contrib import admin


class CheckoutConfig(AppConfig):
    name = 'checkout'


class OrderLineModelInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineModelInline, )


admin.site.register(Order, OrderAdmin)

