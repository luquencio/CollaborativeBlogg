from django.shortcuts import render
from django.http import HttpResponse
import urllib

# Create your views here.

def home(request):
	f = urllib.request.urlopen("http://google.com")
	g = f.read()
	f.close()

	return HttpResponse(g)


def post(request,id_post):
	html = post.object.get(pk = id).title
	return HttpResponse(html)