from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'Web.views.home', name='home'),
    url(r'^loans/$', 'loans.views.index'), 
    url(r'^loans/(?P<loan_id>\d+)/$', 'loans.views.detail'),
    url(r'^loans/(?P<loan_id>\d+)/results/$', 'loans.views.results'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
