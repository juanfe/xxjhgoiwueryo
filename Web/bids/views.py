from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from bids.models import Bid
from django.http import HttpResponse
from datetime import datetime

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
