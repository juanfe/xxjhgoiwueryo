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
