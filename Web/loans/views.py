from django.template import RequestContext, loader
from loans.models import Loan, MortgageOriginator
from django.http import HttpResponse

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
    latest_loan_list = Loan.objects.all().order_by('-Creation')[:10]
    t = loader.get_template('listloans.html')
    c = RequestContext({
		'latest_loan_list': latest_loan_list,
    })
    return HttpResponse(t.render(c))

def detail(request, loan_id):
	return HttpResponse("You are at loan %s." % loan_id)

def results(request, loan_id):
	return HttpResponse("You are at result of loan %s." % loan_id)


