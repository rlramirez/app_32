from django.conf.urls import patterns, include, url
from django.contrib import admin
from protal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_32.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'protal.views.inicio', name='inicio'),
    url(r'^productos/', 'protal.views.productos', name='productos'),
    url(r'^servicios/', 'protal.views.servicios', name='servicios'),
    url(r'^clientes/', 'protal.views.clientes', name='clientes'),
    url(r'^contactos/', 'protal.views.contactos', name='contactos'),
    url(r'^mapa/', 'protal.views.mapa', name='mapa'),
    url(r'^chart/', 'protal.views.chart', name='chart'),
    url(r'^admin/', include(admin.site.urls)),
)
