#!/usr/bin/python

from LiqSpot import LiqEngine

eng = LiqEngine()

eng.setMortgageOperators(['ABC Mortgage', 'Prime Lending', 'Best Loans Inc',
		'Integrity Lending'])

eng.setLoans([{'Loand Id' : '1', 'Mortgage Operator': 'ABC Mortgage', 'Load Amount': 318725.0},
	{'Loand Id' : '2', 'Mortgage Operator': 'ABC Mortgage', 'Load Amount': 375685.0},
	{'Loand Id' : '3', 'Mortgage Operator': 'Prime Lending', 'Load Amount': 479875.0},
	{'Loand Id' : '4', 'Mortgage Operator': 'Prime Lending', 'Load Amount': 525400.0},
	{'Loand Id' : '5', 'Mortgage Operator': 'Best Loans Inc', 'Load Amount': 515425.0},
	{'Loand Id' : '6', 'Mortgage Operator': 'Integrity Lending', 'Load Amount': 485000.0}])

eng.setUsers([{'User Id' : '1104143@test.com', 'Funds available': 500000.0},
			{'User Id' : '1104145@test.com', 'Funds available': 752000.0},
			{'User Id' : '1104133@test.com', 'Funds available': 418000.0},
			{'User Id' : '1104149@test.com', 'Funds available': 47000.0},
			{'User Id' : '1104161@test.com', 'Funds available': 292000.0},
			{'User Id' : '1104139@test.com', 'Funds available': 250000.0}, 
			{'User Id' : '1104136@test.com', 'Funds available': 860000.0},
			{'User Id' : '1104151@test.com', 'Funds available': 283000.0},
			{'User Id' : '1104138@test.com', 'Funds available': 300000.0},
			{'User Id' : '1104157@test.com', 'Funds available': 629000.0},
			{'User Id' : '1104155@test.com', 'Funds available': 639000.0},
			{'User Id' : '1104156@test.com', 'Funds available': 274000.0},
			{'User Id' : '1104131@test.com', 'Funds available': 598000.0},
			{'User Id' : '1104154@test.com', 'Funds available': 185000.0},
			{'User Id' : '1104159@test.com', 'Funds available': 532000.0},
			{'User Id' : '1104158@test.com', 'Funds available': 562000.0}, 
			{'User Id' : '1104141@test.com', 'Funds available': 285000.0},
			{'User Id' : '1104134@test.com', 'Funds available': 187500.0},
			{'User Id' : '1104140@test.com', 'Funds available': 74000.0},
			{'User Id' : '1104152@test.com', 'Funds available': 1500000.0}])
