from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from article.models import Customer, Order, Product, Image, Category, Order_Product

def articles(request):
	args = {}
	args['product_all'] = Product.objects.all()
	args['product_images'] = Image.objects.all()
	return render_to_response('articles.html', args)