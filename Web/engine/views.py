from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from loans.models import Loan, MortgageOriginator
from django.http import HttpResponse
from datetime import datetime
from LiqSpot import LiqEngine
from models import Loan, Bid, UserFunds 

def calc(request):
	eng = LiqEngine()
	#TODO add LSSpread and PriorDayRateUsed from config
	eng.setParameters(LSSpread = 1, PriorDayRateUsed = 3.5)
	eng.setLoans([{'loanId' : '1', 'mortgageOriginator': 'ABC Mortgage',
					'loanAmount': 318725.0},
			{'loanId' : '2', 'mortgageOriginator': 'ABC Mortgage',
					'loanAmount': 375685.0},
			{'loanId' : '3', 'mortgageOriginator': 'Prime Lending',
					'loanAmount': 479875.0},
			{'loanId' : '4', 'mortgageOriginator': 'Prime Lending',
					'loanAmount': 525400.0},
			{'loanId' : '5', 'mortgageOriginator': 'Best Loans Inc',
					'loanAmount': 515425.0},
			{'loanId' : '6', 'mortgageOriginator': 'Integrity Lending',
					'loanAmount': 485000.0}])
	eng.setUsers([{'userId' : '1104145@test.com', 'fundsAvailable': 752000.0},
			{'userId' : '1104133@test.com', 'fundsAvailable': 418000.0},
			{'userId' : '1104149@test.com', 'fundsAvailable': 47000.0},
			{'userId' : '1104161@test.com', 'fundsAvailable': 292000.0},
			{'userId' : '1104136@test.com', 'fundsAvailable': 860000.0},
			{'userId' : '1104151@test.com', 'fundsAvailable': 283000.0},
			{'userId' : '1104156@test.com', 'fundsAvailable': 274000.0},
			{'userId' : '1104159@test.com', 'fundsAvailable': 532000.0},
			{'userId' : '1104158@test.com', 'fundsAvailable': 562000.0},
			{'userId' : '1104140@test.com', 'fundsAvailable': 74000.0}])
	eng.setBids([{'date' : '2012-01-12', 'time' : '17:06:12', 'bidId' : '1104136',
			'userId': '1104136@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '4',
			'orderType' : 'Competitive', 'bidRate' : 6.000,
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-12', 'time' : '19:59:00', 'bidId' : '1104140',
			'userId' : '1104140@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '5',
			'orderType' : 'Competitive', 'bidRate' : 2.500,
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-12', 'time' : '21:39:48', 'bidId' : '1104159',
			'userId' : '1104159@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '1',
			'orderType' : 'Noncompetitive', 'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-12', 'time' : '23:06:12', 'bidId' : '1104161',
			'userId': '1104161@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '4',
			'orderType' : 'Noncompetitive', 'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-12', 'time' : '23:35:00', 'bidId' : '1104145',
			'userId' : '1104145@test.com', 'bidType' : 'Specified',
			'Participation' : 10, 'assetSubset' : 'Loan', 'loanId' : '1',
			'orderType' : 'Competitive', 'bidRate' : 1.500,
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-13', 'time' : '2:23:00', 'bidId' : '1104133',
			'userId' : '1104133@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '4',
			'orderType' : 'Competitive', 'bidRate' : 4.000,
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-13', 'time' : '2:27:48', 'bidId' : '1104149',
			'userId' : '1104149@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan',
			'loanId' : '5', 'orderType' : 'Noncompetitive',
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-13', 'time' : '3:54:12', 'bidId' : '1104151',
			'userId' : '1104151@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan',
			'loanId' : '1', 'orderType' : 'Noncompetitive',
			'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-13', 'time' : '7:30:12', 'bidId' : '1104156',
			'userId' : '1104156@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '2',
			'orderType' : 'Noncompetitive', 'orderTiming' : 'Day Trade'},
		{'date' : '2012-01-13', 'time' : '8:56:36', 'bidId' : '1104158',
			'userId' : '1104158@test.com', 'bidType' : 'Specified',
			'Participation' : 20, 'assetSubset' : 'Loan', 'loanId' : '1',
			'orderType' : 'Competitive', 'bidRate' : 2.250,
			'orderTiming' : 'Day Trade'}])
	try:
		#todo mirar como es el cuento para 
		context = eng.Calc()
		# Fill Loans in the engine's loans
		Loan.objects.all().delete()
		for l in context['loans'].iteritems():
			nl = Loan()
			nl.Loanid = l[0]
			nl.Funded = l[1]['funded']
			nl.InvestorRate = l[1]['investorRate']
			#TODO search the RateToMo and FundedAmount
			nl.RateToMo = 0
			nl.FundedAmount = 0
			nl.save()
		# Fill Bids in the engine's bids
		Bid.objects.all().delete()
		# NOTE: Take care erasing BidsAllocation, because it erase in cascade
		#BidsAllocation.objects.all().delete()
		for b in context['bids'].iteritems():
			nb = Bid()
			nb.save()
		# Fill Users in the engine's User
		UserFunds.objects.all().delete()
		for u in context['users'].iteritems():
			nu = UserFunds()
			nu.User = u[0]
			nu.Funds = u[1]['fundsAvailable']
			nu.save() 

		return render_to_response("engine/results.html", context)
	except:
		return render_to_response("500.html")
