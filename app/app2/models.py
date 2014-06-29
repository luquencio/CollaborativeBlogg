from django.db import models

# Create your models here.
class Catetoria(models.Model):
	titulo = models.CharField(max_length = 200)

class Enlace(models.Model):
	titulo = models.CharField(max_length = 200)
	enlace = models.URLField()
	votos = models.IntegerField(default = 0) 