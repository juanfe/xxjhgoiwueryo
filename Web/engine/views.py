from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from models import Loan, MortgageOriginator
from django.http import HttpResponse
from datetime import datetime

def calc(request):
    context = {}
    return render_to_response("engine/results.html", context)
