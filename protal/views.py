from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

def productos(request):
	return render_to_response('productos.html', context_instance=RequestContext(request))

def clientes(request):
	return render_to_response('clientes.html', context_instance=RequestContext(request))	

def servicios(request):
	return render_to_response('servicios.html', context_instance=RequestContext(request))	

def contactos(request):
	return render_to_response('contactos.html', context_instance=RequestContext(request))		

def mapa(request):
	return render_to_response('mapa.html', context_instance=RequestContext(request))		