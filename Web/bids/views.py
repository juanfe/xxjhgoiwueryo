from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect, get_object_or_404
from bids.models import Bid
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import UserInGroup
#from bids.forms import DojoBidForm, BidForm
from bids.forms import BidForm

def index(request):
    context = {}
    return render_to_response("bids/list_bids.html", context)

def detail(request, bid_id):
    b = get_object_or_404(Bid, pk=bid_id)
    return render_to_response('bids/detail.html', {'bid', b},
        context_instance=RequestContext(request))
    #HttpResponse("You're detail %s." % bid_id)

def results(request, bid_id):
    HttpResponse("You're result  %s." % bid_id)

def addbid(request, bid_id):
    b = get_object_or_404(Bid, pk=bid_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('bids/detail.html', {
            'bid': b,
            'error_message': "You didn't select a choice.",
        }, context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('bids.views.results', args=(b.id)))

def initial_data(request):
    b = Bid(User = "1104134",
            CreatedAt = datetime.strptime("2/1/2012 3:00:00 PM","%m/%d/%Y %H:%M:%S %p").date(),
            ExpiresAt = datetime.strptime("2/1/2012 3:00:00 PM","%m/%d/%Y %H:%M:%S %p").date(),
            Type = "G", Aggregated=15000000, Participation = 10, Competitive = False,
            OrderTiming = "A", FundsAvailable = 187500)
    b.save()
    return HttpResponse("Initial data was readed")

def MyBids(request):
	try:
		return render_to_response("mybids.html",
			context_instance=RequestContext(request))
	except:
		return render_to_response("500.html",
			context_instance=RequestContext(request))

#@login_required
#@user_passes_test(lambda u: UserInGroup(u, ["Admin"]),
#		login_url='/accounts/login/?next=/bids/addbid/')
#def FormAddBid(request):#, id): #The id is passed in the url like /(?P<id>.+)/ 
#	#Context = {'loans': ""}
#	try:
#		bid = Bid.objects.create()
#		form = DojoBidForm(instance=bid)
#		default_form = BidForm(instance=bid)
#		#return render_to_response("bids/formaddbid.html", Context,
#		return render_to_response("bids/formaddbid.html", locals(),
#				context_instance=RequestContext(request))
#	except:
#		return render_to_response("500.html",
#				context_instance=RequestContext(request))

def FormBid(request):
	latest_bid_list = Bid.objects.all().order_by('User')

	return render_to_response('bids/formbid.html',
			{'latest_bid_list': latest_bid_list},
			context_instance=RequestContext(request))

def FormAddBid(request):
    # sticks in a POST or renders empty form
    form = BidForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        cmodel.save()
        return redirect(FormBid)

    return render_to_response('bids/formaddbid.html',
                              {'bid_form': form},
                              context_instance=RequestContext(request))
                              
