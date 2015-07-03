from django.conf.urls import patterns, include, url
from django.contrib import admin
from protal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_32.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'protal.views.inicio', name='inicio'),
    url(r'^admin/', include(admin.site.urls)),
)
