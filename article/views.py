from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from article.models import Customer, Order, Product, Image, Category, Order_Product

def articles(request):
	args = {}
	args['product_all'] = Product.objects.all()
	args['product_images'] = Image.objects.all()
	args['product_categories'] = Category.objects.all()
	return render_to_response('articles.html', args)

def article(request, product_id=1):
	args = {}
	args['product'] = Product.objects.get(id = product_id)
	args['image'] = Image.objects.filter(product__id__contains = product_id)
	return render_to_response('article.html', args)