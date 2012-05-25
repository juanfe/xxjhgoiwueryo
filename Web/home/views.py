from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from loans.models import Loan, MortgageOriginator
from django.http import HttpResponse
from users.utils import is_logged_in, UserName, GetUserGroups

def HomePage(request):
	try:
		Context = {'is_logged_in': is_logged_in(request)}
		Context['User'] = UserName(request)
		Context['Groups'] = GetUserGroups(request)
		print Context
		return render_to_response("home.html", Context,
				context_instance=RequestContext(request))
	except:
		return render_to_response("500.html",
				context_instance=RequestContext(request))
