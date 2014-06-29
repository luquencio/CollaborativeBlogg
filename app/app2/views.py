from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime 
from django.shortcuts import render_to_response
from app2.models import * 


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