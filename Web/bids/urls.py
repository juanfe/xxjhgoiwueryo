from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bids.views',
	url(r'^$', 'index'),
	url(r'^initial_data/$', 'initial_data'),
	url(r'^mybids/$', 'MyBids'),
	url(r'^bids/$', 'FormBid'),
	url(r'^bidadd/$', 'FormAddBid'),
	url(r'^bidedit/(?P<bid_id>\d+)/$', 'FormEditBid'),
	url(r'^biddel/(?P<bid_id>\d+)/$', 'DelBid'),
)
