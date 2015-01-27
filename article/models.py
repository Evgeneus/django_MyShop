# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
#Customer table
class Customer(models.Model):
	first_name = models.CharField(max_length = 30, verbose_name = "Имя")
	second_name = models.CharField(max_length = 30, verbose_name = "Фамилия")
	phone_number = models.BigIntegerField(default = 0, verbose_name = "Номер мобильного")
	email_addres = models.EmailField(verbose_name = "email-адрес")
	city_addres = models.CharField(max_length = 30, verbose_name = "Город")

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.second_name)

	class Meta():
		db_table = "Customer"

#Category table
class Category(models.Model):
	category = models.CharField(max_length = 70, verbose_name = "Категории")

	def __unicode__(self):
		return u'%s' % self.category

	class Meta():
		db_table = "Category"

#Product table
class Product(models.Model):
	product_title = models.CharField(max_length = 70, verbose_name = "Наименование продукта")
	description = models.TextField(verbose_name = "Описание продукта")
	price_ye = models.FloatField(verbose_name = "Цена(в у. е.)")
	amount = models.IntegerField(default = 0, verbose_name = "Количество на склажде")
	product_category = models.ForeignKey(Category, null=True, verbose_name = "Категории")

	def __unicode__(self):
		return u'%s' % self.product_title

	class Meta():
		db_table = "Product"

#Order table
class Order(models.Model):
	order_date = models.DateTimeField(verbose_name = "Дата заказа")
	orders_sum = models.FloatField(verbose_name = "Сумма заказа")
	order_customer = models.ForeignKey(Customer, verbose_name = "Заказчик")
	products = models.ManyToManyField(Product, verbose_name = "Перечень заказа")

	def __unicode__(self):
		return u'%s' % self.order_date

	class Meta():
		db_table = "Order"

#Order_Product table
class Order_Product(models.Model):
	order = models.ForeignKey(Order, verbose_name = "Заказчик")
	product = models.ForeignKey(Product, verbose_name = "Наименование товара")
	kol_product = models.IntegerField(default = 0, verbose_name = "Количество товара")
	sum_product = models.FloatField(default = 0, verbose_name = "Сумма, у. е.")

	def __unicode__(self):
		return u'%s' % self.product

	class Meta():
		db_table = "Order_Product"


#Images table
class Image(models.Model):
	product = models.OneToOneField(Product)
	top_image = models.ImageField(verbose_name ="Главное изображение")
	second_image = models.ImageField(blank = True, verbose_name = "Изображение 2")
	third_image = models.ImageField(blank = True, verbose_name = "Изображение 3")
	fourth_image = models.ImageField(blank = True, verbose_name = "Изображение 4")
	fifth_image = models.ImageField(blank = True, verbose_name = "Изображение 5")

	def __unicode__(self):
		return u'%s' % self.product

	class Meta():
		db_table = "Image"