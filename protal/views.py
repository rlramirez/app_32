from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
	#return render_to_response('iniciod.html', context_instance=RequestContext(request))
	return render_to_response('inicio.html',
                          {"foo": "bar"},
                          context_instance=RequestContext(request))


	#return HttpResponse('Esta es mi primera vista!')