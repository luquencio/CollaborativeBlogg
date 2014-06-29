from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime 


# Create your views here.
def hora_actual(request):
	ahora = datetime.now()
	t = get_template('hora.html')
	c = Context({'hora':ahora})
	html = t.render(c)
	return HttpResponse(html)  