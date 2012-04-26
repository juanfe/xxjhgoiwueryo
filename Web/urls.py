from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^admin/', include(admin.site.urls)),
    url(r'^mo/$', 'loans.views.moindex'), 
    url(r'^loans/$', 'loans.views.index'), 
    url(r'^loans/(?P<loan_id>\d+)/$', 'loans.views.detail'),
    url(r'^loans/(?P<loan_id>\d+)/results/$', 'loans.views.results'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^initial_data/$', include('initial_data')),
	url(r'^dojango/', include('dojango.urls')),
    ('^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'home.html'}),
)
