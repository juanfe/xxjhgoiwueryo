from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from loans.models import Loan, MortgageOriginator
from django.http import HttpResponse
from users.utils import UserContext 

def HomePage(request):
	try:
		Context = UserContext(request)
		print Context
		return render_to_response("home.html", Context,
				context_instance=RequestContext(request))
	except:
		return render_to_response("500.html",
				context_instance=RequestContext(request))
