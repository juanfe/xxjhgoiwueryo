from datetime import datetime
from LiqSpot import LiqEngine
from model import loansModel
from google.appengine.ext import db
#from google.appengine.ext.db import Key

def calct():
	eng = LiqEngine()
	#TODO add LSSpread and PriorDayRateUsed from config
	eng.setParameters(LSSpread = 1, PriorDayRateUsed = 3.5)

	#TODO only set loans who are involved in the calc
	loans = db.GqlQuery("SELECT * "
			"FROM loansModel ")
	s = []
	for l in loans:
		s.append({'loanId' : l.collateral_key ,
				'mortgageOriginator': l.property_type_code ,
				 'loanAmount': l.curr_upb})

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

	users = db.GqlQuery("SELECT * "
			"FROM User ")
	usr = []
	for u in users:
		usr.append({'userId' : u.account,
				'fundsAvailable': u.fundsAvailable })

	eng.setUsers([{'userId' : '1104134@test.com', 'fundsAvailable': 187500.0},
			{'userId' : '1104143@test.com', 'fundsAvailable': 500000.0},
			{'userId' : '1104154@test.com', 'fundsAvailable': 185000.0},
			{'userId' : '1104152@test.com', 'fundsAvailable': 1500000.0},
			{'userId' : '1104136@test.com', 'fundsAvailable': 860000.0},
			{'userId' : '1104138@test.com', 'fundsAvailable': 300000.0},
			{'userId' : '1104139@test.com', 'fundsAvailable': 250000.0},
			{'userId' : '1104140@test.com', 'fundsAvailable': 74000.0},
			{'userId' : '1104141@test.com', 'fundsAvailable': 285000.0},
			{'userId' : '1104159@test.com', 'fundsAvailable': 532000.0},
			{'userId' : '1104161@test.com', 'fundsAvailable': 292000.0},
			{'userId' : '1104145@test.com', 'fundsAvailable': 752000.0},
			{'userId' : '1104133@test.com', 'fundsAvailable': 418000.0},
			{'userId' : '1104149@test.com', 'fundsAvailable': 47000.0},
			{'userId' : '1104151@test.com', 'fundsAvailable': 283000.0},
			{'userId' : '1104131@test.com', 'fundsAvailable': 598000.0},
			{'userId' : '1104155@test.com', 'fundsAvailable': 639000.0},
			{'userId' : '1104156@test.com', 'fundsAvailable': 274000.0},
			{'userId' : '1104157@test.com', 'fundsAvailable': 629000.0},
			{'userId' : '1104158@test.com', 'fundsAvailable': 562000.0}])

	eng.setBids([{'date' : '15:00:00', 'bidId' : '1104134',
				'userId' : '1104134@test.com', 'bidType' : 'General',
				'Aggregate' : 500000.0, 'Participation' : 10,
				'orderType' : 'Noncompetitive', 'bidRate' : 3.000,
				'orderTiming' : 'Auto'},
			{'date' : '15:00:00', 'bidId' : '1104143',
				'userId' : '1104143@test.com', 'bidType' : 'Specified',
				'Aggregate' : 500000.0, 'Participation' : 20,
				'assetSubset' : 'Loan', 'loanId' : '1',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.875,
				'orderTiming' : 'Auto'},
			{'date' : '15:00:00', 'bidId' : '1104154',
				'userId' : '1104154@test.com', 'bidType' : 'General',
				'Aggregate' : 100000.0, 'Participation' : 10,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.000,
				'orderTiming' : 'Auto'},
			{'date' : '15:00:00', 'bidId' : '1104152',
				'userId' : '1104152@test.com', 'bidType' : 'Specified',
				'Aggregate' : 100000.0, 'Participation' : 30,
				'assetSubset' : 'Loan', 'loanId' : '3',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.500,
				'orderTiming' : 'Auto'},
			{'date' : '17:06:12', 'bidId' : '1104136',
				'userId' : '1104136@test.com', 'bidType' : 'General',
				'Aggregate' : 500000.0, 'Participation' : 10,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.750,
				'orderTiming' : 'Day Trade'},
			{'date' : '18:32:36', 'bidId' : '1104138',
				'userId' : '1104138@test.com', 'bidType' : 'Specified',
				'Aggregate' : 500000.0, 'Participation' : 10,
				'assetSubset' : 'Loan', 'loanId' : '5',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.625,
				'orderTiming' : 'Day Trade'},
			{'date' : '19:15:48', 'bidId' : '1104139',
				'userId' : '1104139@test.com', 'bidType' : 'General',
				'Aggregate' : 100000.0, 'Participation' : 20,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.250,
				'orderTiming' : 'Day Trade'},
			{'date' : '19:59:00', 'bidId' : '1104140',
				'userId' : '1104140@test.com', 'bidType' : 'Specified',
				'Aggregate' : 100000.0, 'Participation' : 20,
				'assetSubset' : 'MO', 'mortgageOriginator' : 'ABC Mortgage',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.875,
				'orderTiming' : 'Day Trade'},
			{'date' : '20:42:12', 'bidId' : '1104141',
				'userId' : '1104141@test.com', 'bidType' : 'General',
				'Aggregate' : 500000.0, 'Participation' : 30,
				'orderType' : 'Noncompetitive', 'bidRate' : 3.000,
				'orderTiming' : 'Day Trade'},
			{'date' : '21:39:48', 'bidId' : '1104159',
				'userId' : '1104159@test.com', 'bidType' : 'Specified',
				'Aggregate' : 500000.0, 'Participation' : 30,
				'assetSubset' : 'Loan', 'loanId' : '3',
				'orderType' : 'Noncompetitive', 'bidRate' : 3.125,
				'orderTiming' : 'Day Trade'},
			{'date' : '23:06:12', 'bidId' : '1104161',
				'userId' : '1104161@test.com', 'bidType' : 'General',
				'Aggregate' : 100000.0, 'Participation' : 40,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.500,
				'orderTiming' : 'Day Trade'},
			{'date' : '23:35:00', 'bidId' : '1104145',
				'userId' : '1104145@test.com', 'bidType' : 'Specified',
				'Aggregate' : 100000.0, 'Participation' : 30,
				'assetSubset' : 'Loan', 'loanId' : '1',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.375,
				'orderTiming' : 'Day Trade'},
			{'date' : '2:23:00', 'bidId' : '1104133',
				'userId' : '1104133@test.com', 'bidType' : 'General',
				'Aggregate' : 500000.0, 'Participation' : 20,
				'orderType' : 'Noncompetitive', 'bidRate' : 3.500,
				'orderTiming' : 'Day Trade'},
			{'date' : '2:27:48', 'bidId' : '1104149',
				'userId' : '1104149@test.com', 'bidType' : 'Specified',
				'Aggregate' : 500000.0, 'Participation' : 10,
				'assetSubset' : 'Loan', 'loanId' : '1',
				'orderType' : 'Noncompetitive', 'bidRate' : 3.375,
				'orderTiming' : 'Day Trade'},
			{'date' : '3:54:12', 'bidId' : '1104151',
				'userId' : '1104151@test.com', 'bidType' : 'General',
				'Aggregate' : 100000.0, 'Participation' : 20,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.125,
				'orderTiming' : 'Day Trade'},
			{'date' : '4:37:24', 'bidId' : '1104131',
				'userId' : '1104131@test.com', 'bidType' : 'Specified',
				'Aggregate' : 100000.0, 'Participation' : 30,
				'assetSubset' : 'MO', 'mortgageOriginator' : 'Prime Lending',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.500,
				'orderTiming' : 'Day Trade'},
			{'date' : '6:47:00', 'bidId' : '1104155',
				'userId' : '1104155@test.com', 'bidType' : 'General',
				'Aggregate' : 500000.0, 'Participation' : 20,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.875,
				'orderTiming' : 'Day Trade'},
			{'date' : '7:30:12', 'bidId' : '1104156',
				'userId' : '1104156@test.com', 'bidType' : 'Specified',
				'Aggregate' : 500000.0, 'Participation' : 10,
				'assetSubset' : 'Loan', 'loanId' : '1',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.500,
				'orderTiming' : 'Day Trade'},
			{'date' : '8:13:24', 'bidId' : '1104157',
				'userId' : '1104157@test.com', 'bidType' : 'General',
				'Aggregate' : 100000.0, 'Participation' : 10,
				'orderType' : 'Noncompetitive', 'bidRate' : 2.000,
				'orderTiming' : 'Day Trade'},
			{'date' : '8:56:36', 'bidId' : '1104158',
				'userId' : '1104158@test.com', 'bidType' : 'Specified',
				'Aggregate' : 100000.0, 'Participation' : 10,
				'assetSubset' : 'Loan', 'loanId' : '3',
				'orderType' : 'Noncompetitive', 'bidRate' : 2.125,
				'orderTiming' : 'Day Trade'}])
	return eng.Calc()

def calc():
	try:
		context = calct()

		Context = {}
		Context['loans'] = []
		for c in context['loans'].iteritems():
			Context['loans'].append(c[0])
		Context['bids'] = []
		for b in context['bids'].iteritems():
			c = [{'bid': b[0]}]
			for l in Context['loans']:
				if l in b[1]['allocatedAmounts']:
					c.append(({"key": l, "val": '%.2f' % b[1]['allocatedAmounts'][l]}))
				else:
					c.append(({"key": l, "val": 0}))
			Context['bids'].append(c)
		loans = db.GqlQuery("SELECT * "
				"FROM loansModel ")
		s = ""
		for l in loans:
			s = s +("%s "%l.customer_account_key)
		#Context['tempo'] = []
		Context['tempo'] = s
		#for l in loans.iteritems():
		#	Context['tempo'].append(l['key_name'])
		return Context
	except:
		return None
