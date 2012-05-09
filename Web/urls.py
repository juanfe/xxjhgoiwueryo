from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

#handler500 = 'djangotoolbox.errorviews.server_error'
handler500 = 'templates.500.html'
handler404 = 'templates.404.html'
handler403 = 'templates.403.html'

urlpatterns = patterns('',
	('^_ah/warmup$', 'djangoappengine.views.warmup'),
	url(r'^home/$', 'home.views.HomePage'),
	url(r'^search/$', 'search.views.SearchPage'), 
	url(r'^mo/$', 'loans.views.moindex'), 
	url(r'^loans/', include('loans.urls')), 
	url(r'^bids/', include('bids.urls')),
	url(r'^polls/', include('polls.urls')),
	url(r'^myapp/', include('myapp.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^calc/', include('engine.urls')),
	#url(r'^initial_data/$', include('initial_data')),
	url(r'^dojango/', include('dojango.urls')),
	url(r'^tbl/', include('test_app.urls')),
	('^$', 'django.views.generic.simple.direct_to_template',
		{'template': 'home.html'}),
)
