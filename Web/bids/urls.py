from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bids.views',
	url(r'^$', 'index'),
	url(r'^initial_data/$', 'initial_data'),
	url(r'^mybids/$', 'MyBids'),
	url(r'^bids/$', 'FormBid'),
	url(r'^bidadd/$', 'FormAddBid'),
)
