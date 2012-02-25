import datetime

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
				{'MO': 'Total', 'Load Amount': 2700110.0}],
		'test_LoadBids' : { 'p' : 20,
			'q' : '1104154',
			'r' : {'loannum': '2',
				'dateorder': datetime.datetime(2012, 1, 5, 9, 16), 'funds': 185000.0,
				'mo': '', 'time': datetime.datetime(1900, 1, 1, 15, 0),
				'bidrate': 0.03, 'competitive': True, 'ordertiming': 'Auto',
				'lorm': 'Loan', 'specified': True, 'aggregate': '', 'sperate': 0.2,
				'genrate': ''},},
		'test_SpecifiedAssetAssignation' : {'1104139': [63745.0, 0, 0, 0, 0, 0, 63745.0],
					'1104138': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104161': [0, 0, 0, 105080.0, 0, 0, 105080.0],
					'1104152': [0, 0, 95975.0, 105080.0, 0, 0, 201055.0],
					'1104131': [0, 0, 0, 105080.0, 0, 0, 105080.0],
					'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
					'1104134': [63745.0, 0, 0, 0, 0, 0, 63745.0],
					'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
					'1104140': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104141': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104151': [63745.0, 0, 0, 0, 0, 0, 63745.0],
					'1104143': [63745.0, 75137.0, 0, 0, 0, 0, 138882.0],
					'1104157': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
					'1104155': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104154': [0, 75137.0, 0, 0, 0, 0, 75137.0],
					'1104149': [0, 0, 0, 0, 103085.0, 0, 103085.0],
					'1104159': [63745.0, 0, 0, 0, 0, 0, 63745.0],
					'1104158': [63745.0, 0, 0, 0, 0, 0, 63745.0],
					'1104156': [0, 75137.0, 0, 0, 0, 0, 75137.0],
					'Total': [414342.5, 225411.0, 95975.0, 525400.0, 618510.0, 0, 1879638.5]},
		'test_WARateSC' : [0.028269230769230772, 0.030000000000000002, 0.03,
					0.04025, 0.025625, None, 0.031043944088185043],
		'test_CalcRemaing' : [(-95617.5, 'over'), (150274.0, 'under'),
                                (383900.0, 'under'), (0, None), (-103085.0, 'over'),
                                (485000.0, 'under'), (820471.5, 'under')],
		}
