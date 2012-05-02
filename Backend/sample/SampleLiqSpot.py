#!/usr/bin/python
from pprint import pprint
from LiqSpot import LiqEngine

eng = LiqEngine()

eng.setParameters(LSSpread = 1, PriorDayRateUsed = 3.5)

eng.setMortgageOriginator(['ABC Mortgage', 'Prime Lending', 'Best Loans Inc',
		'Integrity Lending'])

eng.setLoans([{'loanId' : '1', 'mortgageOriginator': 'ABC Mortgage', 'loanAmount': 318725.0},
	{'loanId' : '2', 'mortgageOriginator': 'ABC Mortgage', 'loanAmount': 375685.0},
	{'loanId' : '3', 'mortgageOriginator': 'Prime Lending', 'loanAmount': 479875.0},
	{'loanId' : '4', 'mortgageOriginator': 'Prime Lending', 'loanAmount': 525400.0},
	{'loanId' : '5', 'mortgageOriginator': 'Best Loans Inc', 'loanAmount': 515425.0},
	{'loanId' : '6', 'mortgageOriginator': 'Integrity Lending', 'loanAmount': 485000.0}])

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

eng.Calc()

pprint(eng.Data)
