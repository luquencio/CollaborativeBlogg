from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime 
from django.shortcuts import render_to_response
from app2.models import * 
from django.shortcuts import get_object_or_404
from app2.forms import * 
from django.template.context import RequestContext

# Create your views here.

def home(request ):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"
	local = {"categorias":categorias, "enlaces":enlaces}
	return render_to_response(template, local)

def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html',{'hora':now})

def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos =- 1
	enlace.save()
	return HttpResponseRedirect("/")

def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos =+ 1
	enlace.save()
	return HttpResponseRedirect("/")

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk = id_categoria )
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html" 
	return render_to_response(template, locals())

def add(request):
	categorias = Categoria.objects.all()
	
	if request.method == 'POST':
		form = EnlaceForm(request.POST)
		if form.is_valid(): 
			form.save()

			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm() 

	template = "form.html"
	return render_to_response(template,
		context_instance = RequestContext(request,locals()))