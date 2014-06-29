from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime 
from django.shortcuts import render_to_response


# Create your views here.


def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html',{'hora':now})