from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from article.models import Customer, Order, Product, Image, Category, Order_Product

#custom context processor

def custom_proc(request):
	return {
		'product_categories' : Category.objects.all()
	}


def articles(request):
	args = {}
	args['products'] = Product.objects.all()
	return render_to_response(
		'articles.html',
		args,
		context_instance = RequestContext(request, processors = [custom_proc])
		)


def article(request, product_id=1):
	args = {}
	args['product'] = Product.objects.get(id = product_id)
	args['image'] = Image.objects.filter(product__id__contains = product_id)
	return render_to_response(
		'article.html',
		args,
		context_instance = RequestContext(request, processors = [custom_proc])
		)


def categorys_product_display(request, category_id = 1):
	args = {}
	args['products'] = Product.objects.filter(product_category_id = category_id)
	return render_to_response(
		'articles.html',
		args, 
		context_instance = RequestContext(request, processors = [custom_proc])
		)


def get_contacts_page(request):
	return render_to_response(
		'contacts.html',
		context_instance = RequestContext(request, processors = [custom_proc])
		)

def get_delivery_page(request):
	return render_to_response(
		'delivery.html',
		context_instance = RequestContext(request, processors = [custom_proc])
		)

def get_discounts_page(request):
	return render_to_response(
		'discounts.html',
		context_instance = RequestContext(request, processors = [custom_proc])
		)