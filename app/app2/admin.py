from django.contrib import admin
from app2.models import *  

# Register your models here.

class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('titulo','enlace', 'votos', 'categoria')

admin.site.register(Categoria)
admin.site.register(Enlace,EnlaceAdmin )
