from django.http import HttpResponse

def index(request):
    return HttpResponse("An application from Vichara Technologies.")

def detail(request, loan_id):
	return HttpResponse("You are at loan %s." % loan_id)

def results(request, loan_id):
	return HttpResponse("You are at result of loan %s." % loan_id)


