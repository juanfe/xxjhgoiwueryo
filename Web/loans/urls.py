import os

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('loans.views',
    url(r'^$', 'index'), 
    url(r'^initial_data/$', 'initial_data'),
    #url(r'^(?P<loan_id>\d+)/$', 'loans.views.detail'),
    #url(r'^(?P<loan_id>\d+)/results/$', 'loans.views.results'),
)
