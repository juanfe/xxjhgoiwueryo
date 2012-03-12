#!/usr/bin/python

from LiqSpot import LiqEngine

eng = LiqEngine()

eng.setMortgageOperators(['ABC Mortgage', 'Prime Lending', 'Best Loans Inc',
		'Integrity Lending'])

eng.setLoans([{'loanId' : '1', 'mortgageOriginator': 'ABC Mortgage', 'loanAmount': 318725.0},
	{'loanId' : '2', 'mortgageOriginator': 'ABC Mortgage', 'loanAmount': 375685.0},
	{'loanId' : '3', 'mortgageOriginator': 'Prime Lending', 'loanAmount': 479875.0},
	{'loanId' : '4', 'mortgageOriginator': 'Prime Lending', 'loanAmount': 525400.0},
	{'loanId' : '5', 'mortgageOriginator': 'Best Loans Inc', 'loanAmount': 515425.0},
	{'loanId' : '6', 'mortgageOriginator': 'Integrity Lending', 'loanAmount': 485000.0}])

eng.setUsers([{'userId' : '1104143@test.com', 'fundsAvailable': 500000.0},
			{'userId' : '1104145@test.com', 'fundsAvailable': 752000.0},
			{'userId' : '1104133@test.com', 'fundsAvailable': 418000.0},
			{'userId' : '1104149@test.com', 'fundsAvailable': 47000.0},
			{'userId' : '1104161@test.com', 'fundsAvailable': 292000.0},
			{'userId' : '1104139@test.com', 'fundsAvailable': 250000.0}, 
			{'userId' : '1104136@test.com', 'fundsAvailable': 860000.0},
			{'userId' : '1104151@test.com', 'fundsAvailable': 283000.0},
			{'userId' : '1104138@test.com', 'fundsAvailable': 300000.0},
			{'userId' : '1104157@test.com', 'fundsAvailable': 629000.0},
			{'userId' : '1104155@test.com', 'fundsAvailable': 639000.0},
			{'userId' : '1104156@test.com', 'fundsAvailable': 274000.0},
			{'userId' : '1104131@test.com', 'fundsAvailable': 598000.0},
			{'userId' : '1104154@test.com', 'fundsAvailable': 185000.0},
			{'userId' : '1104159@test.com', 'fundsAvailable': 532000.0},
			{'userId' : '1104158@test.com', 'fundsAvailable': 562000.0}, 
			{'userId' : '1104141@test.com', 'fundsAvailable': 285000.0},
			{'userId' : '1104134@test.com', 'fundsAvailable': 187500.0},
			{'userId' : '1104140@test.com', 'fundsAvailable': 74000.0},
			{'userId' : '1104152@test.com', 'fundsAvailable': 1500000.0}])

eng.setBids([
