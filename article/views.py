from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

def articles(request):
	
	return render_to_response('articles.html',)
	#html = "<html><body> Hello </body> </html>"
	#return HttpResponse(html)
	#return render(request, '')