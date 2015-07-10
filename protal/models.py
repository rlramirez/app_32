from django.db import models
from django.contrib import admin
# Create your models here.

class lugares(models.Model):
	nombre=models.CharField(max_length=150)
	latitud=models.CharField(max_length=50)
	longitud=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre
	def __str__(self):
		return self.nombre

admin.site.register(lugares)