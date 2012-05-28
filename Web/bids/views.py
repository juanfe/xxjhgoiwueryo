from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect, get_object_or_404
from bids.models import Bid
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import UserInGroup
#from bids.forms import DojoBidForm, BidForm
from bids.forms import BidForm

#def initial_data(request):
#	b = Bid(User = "1104134",
#			CreatedAt = datetime.strptime("2/1/2012 3:00:00 PM","%m/%d/%Y %H:%M:%S %p").date(),
#			ExpiresAt = datetime.strptime("2/1/2012 3:00:00 PM","%m/%d/%Y %H:%M:%S %p").date(),
#			Type = "G", Aggregated=15000000, Participation = 10, Competitive = False,
#			OrderTiming = "A", FundsAvailable = 187500)
#	b.save()
#	return HttpResponse("Initial data was readed")

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin", "Broker"]),
		login_url='/accounts/login/?next=/bids/bids/')
def FormBid(request):
	#latest_bid_list = Bid.objects.all().order_by('User')
	latest_bid_list = Bid.objects.all()

	return render_to_response('bids/formbid.html',
			{'latest_bid_list': latest_bid_list},
			context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin", "Broker"]),
		login_url='/accounts/login/?next=/bids/bidadd/')
def FormAddBid(request):
	# sticks in a POST or renders empty form
	form = BidForm(request.POST or None)
	if form.is_valid():
		cmodel = form.save(commit = False)
		cmodel.User = request.user
		cmodel.Status = 'A'
		#TODO check if there are enouf funds, Participation < 100 and competitive bid rate < 100
		#TODO Set status also
		cmodel.save()
		return redirect(FormBid)

	return render_to_response('bids/formaddbid.html',
			{'bid_form': form},
			context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin", "Broker"]),
		login_url='/accounts/login/?next=/bids/bids/')
def FormEditBid(request, bid_id):
	bid = get_object_or_404(Bid, pk=bid_id)
	form = BidForm(request.POST or None, instance=bid)
	if form.is_valid():
		bid = form.save()
		#this is where you might choose to do stuff.
		#contact.name = 'test'
		bid.save()
		return redirect(FormBid)

	return render_to_response('bids/formeditbid.html',
			{'bid_form': form, 'bid_id': bid_id},
			context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin", "Broker"]),
		login_url='/accounts/login/?next=/bids/bids/')
def DelBid(request, bid_id):
	c = Bid.objects.get(pk=bid_id).delete()

	return redirect(FormBid)
