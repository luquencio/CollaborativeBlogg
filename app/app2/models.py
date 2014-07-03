from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.titulo

class Enlace(models.Model):
	titulo = models.CharField(max_length = 200)
	enlace = models.URLField()
	votos = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria)
	usuario = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s - %s" %( self.enlace, self.titulo)


 