from django.template import RequestContext, loader
#import string
from django.shortcuts import render_to_response
from dojango.util.config import Config
from models import Loan, MortgageOriginator
from django.http import HttpResponse
from datetime import datetime
from django.utils import simplejson
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import UserInGroup

def moindex(request):
	m = MortgageOriginator(Name = "juan")
	m.save()
	latest_loan_mo = MortgageOriginator.objects.all().order_by('-Name')[:10]
	t = loader.get_template('loans/moindex.html')
	c = RequestContext({
		'latest_loan_mo': latest_loan_mo,
	})
	return HttpResponse(t.render(c))

def index(request):
	context = {}
	#latest_loan_list = Loan.objects.all().order_by('-Creation')[:10]
	#t = loader.get_template('listloans.html')
	#c = RequestContext({
	#	'latest_loan_list': latest_loan_list,
	#})
	#return HttpResponse(t.render(c))
	return render_to_response("loans/list_loans.html", context)

def detail(request, loan_id):
	return HttpResponse("You are at loan %s." % loan_id)

def results(request, loan_id):
	return HttpResponse("You are at result of loan %s." % loan_id)

def loansModelInstance(request):
	l = Loan(key_name = 201149912, customer_account_key="ABCD",
			collateral_key = "201149912", advance_amt = 176021)
	l.state = "WA"
	l.zip = "98606"
	l.orig_upb = 232000
	l.curr_upb = 232000
	l.origination_date = datetime.strptime("2/1/2012","%m/%d/%Y").date()
	l.is_adjustable = False
	l.investor_code = "JPM"
	l.property_type_code = "SFR"
	l.lien_position = 1
	l.original_ltv = 35.8310
	l.original_cltv = 35.8310
	l.fico_score = 741
	l.purpose_code = "CO"
	l.occupancy_code = "O"
	l.doc_level_code = 3
	l.debt_service_ratio = 20.8011040
	l.cur_note_rate = 4.3750
	l.corelogic_fraud_risk_score = 783
	l.corelogic_collateral_risk_score = 323
	l.Hiden = False
	l.save()
	l = Loan(key_name = 201149913, customer_account_key="ABCD",
			collateral_key = "201149913", advance_amt = 176021)
	l.state = "WA"
	l.zip = "98606"
	l.orig_upb = 232000
	l.curr_upb = 232000
	l.origination_date = datetime.strptime("2/1/2012","%m/%d/%Y").date()
	l.is_adjustable = False
	l.investor_code = "JPM"
	l.property_type_code = "SFR"
	l.lien_position = 1
	l.original_ltv = 35.8310
	l.original_cltv = 35.8310
	l.fico_score = 741
	l.purpose_code = "CO"
	l.occupancy_code = "O"
	l.doc_level_code = 3
	l.debt_service_ratio = 20.8011040
	l.cur_note_rate = 4.3750
	l.corelogic_fraud_risk_score = 783
	l.corelogic_collateral_risk_score = 323
	l.Hiden = False
	l.save()
	return HttpResponse("Initial data was readed")

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin"]),
		login_url='/accounts/login/?next=/loans/listLoans/')
def ListLoans(request):
	l = []
	for _l in Loan.objects.all().values():
		__l = {}
		for k, v in _l.iteritems():
			__l[k] = json.dumps(v, cls = DjangoJSONEncoder)
			if __l[k][0] == '"':
				__l[k] = __l[k][1:-1]
		l.append(__l)

	Context = {'loans': l}
	try:
		return render_to_response("loans/listloans.html", Context,
			context_instance=RequestContext(request))
	except:
		return render_to_response("500.html",
			context_instance=RequestContext(request))
