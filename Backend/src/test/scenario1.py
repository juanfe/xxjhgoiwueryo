argument = ['LiqSpot.py', '-b', '../../sample/bids1.csv', '-l', '../../sample/loans1.csv',
		'True', '-d', ',', '-M', '../mo.csv', '-o', 'test.csv']

scenario = {'test_init' : '../mo.csv',
		'test_LoadMortgageOperators' :
			['ABC Mortgage',  'Prime Lending', 'Best Loans Inc', 'Integrity Lending'],
		'test_addLoans' : { 'p' : ['MO', 'Load Amount', 'Rate'],
			'q' : ['ABC Mortgage', '318725', '0.035'],
			'r' :  [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.035}],
			},
		'test_LoadLoans' :
			[{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.035},
				{'MO': 'ABC Mortgage', 'Load Amount': 375685.0, 'Rate': 0.035},
				{'MO': 'Prime Lending', 'Load Amount': 479875.0, 'Rate': 0.035},
				{'MO': 'Prime Lending', 'Load Amount': 525400.0, 'Rate': 0.035},
				{'MO': 'Best Loans Inc', 'Load Amount': 515425.0, 'Rate': 0.035},
				{'MO': 'Integrity Lending', 'Load Amount': 485000.0, 'Rate': 0.035},
				{'MO': 'Total', 'Load Amount': 2700110.0}]
		}
