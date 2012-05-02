import os
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('engine.views',
    url(r'^$', 'calc'), 
)
