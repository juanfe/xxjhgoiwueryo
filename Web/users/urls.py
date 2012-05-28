from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('users.views',
	url(r'^funds/$', 'funds'),
	url(r'^newfund/$', 'FormNewFund'),
	#url(r'^addfund/(?P<fund_id>\d+)/$', 'FormAddFund'),
)
