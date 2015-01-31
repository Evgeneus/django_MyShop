# -*- coding: utf-8 -*-

from django.contrib import admin
from article.models import Customer, Order, Product, Image, Category, Order_Product

# Register your models here.

class CustomerInline(admin.StackedInline):
	model = Order
	extra = 1

class OrderInline(admin.StackedInline):
	model = Order_Product #Order.products.through
	extra = 1

class CategoryInline(admin.StackedInline):
	model = Product
	extra = 1

class ProductInline(admin.StackedInline):
	model = Image
	extra = 1


class CustomerAdmin(admin.ModelAdmin):
	fields = ['first_name', 'second_name', 'phone_number', 'email_addres', 'city_addres']
	list_filter = ['city_addres']
	inlines = [CustomerInline]


class ProductAdmin(admin.ModelAdmin):
	fields = ['product_title', 'description', 'price_ye', 'amount', 'product_category']
	list_filter = ['amount']
	inlines = [ProductInline]

class OrderAdmin(admin.ModelAdmin):
	fields = ['order_date', 'orders_sum', 'order_customer']
	list_filter = ['order_date']
	inlines = [OrderInline]

class CategoryAdmin(admin.ModelAdmin):
	fields = ['category']
	inlines = [CategoryInline]

class ImageAdmin(admin.ModelAdmin):
	fields = []

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)