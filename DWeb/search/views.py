from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from loans.models import Loan, MortgageOriginator
from django.http import HttpResponse

def SearchPage(request):
	try:
		return render_to_response("search.html",
				context_instance=RequestContext(request))
	except:
		return render_to_response("500.html",
				context_instance=RequestContext(request))
