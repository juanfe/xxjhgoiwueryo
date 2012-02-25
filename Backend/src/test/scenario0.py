import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids0.csv', '-l', '../../sample/loans0.csv',
		'True', '-d', ';', '-M', '../mo.csv', '-o', 'test.csv']

scenario = {'test_init' : '../mo.csv', 
		'test_LoadMortgageOperators' :
			['ABC Mortgage', 'Prime Lending', 'Best Loans Inc', 'Integrity Lending'],
		'test_addLoans' : { 'p' : ['MO', 'Load Amount', 'Rate'],
			'q' : ['ABC Mortgage', ' 318725', ' 0.0225'],
			'r' : [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.0225}],
			},
		'test_LoadLoans' : 
			[{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.0225},
				{'MO': 'ABC Mortgage', 'Load Amount': 375685.0, 'Rate': 0.0225},
				{'MO': 'Prime Lending', 'Load Amount': 479875.0, 'Rate': 0.03},
				{'MO': 'Prime Lending', 'Load Amount': 525400.0, 'Rate': 0.06},
				{'MO': 'Best Loans Inc', 'Load Amount': 515425.0, 'Rate': 0.025},
				{'MO': 'Integrity Lending', 'Load Amount': 485000.0, 'Rate': 0.06},
				{'MO': 'Total', 'Load Amount': 2700110.0}],
		'test_LoadBids' : { 'p' : 20,
			'q' : '1104154',
			'r' : {'loannum': '',
				'dateorder': datetime.datetime(2012, 1, 5, 9, 16), 'funds': 185000.0,
				'mo': '', 'time': datetime.datetime(1900, 1, 1, 15, 0),
				'bidrate': 0.03, 'competitive': True, 'ordertiming': 'Auto', 'lorm': '',
				'specified': False, 'aggregate': 20000000.0, 'sperate': '',
				'genrate': 0.2},},
		'test_SpecifiedAssetAssignation' : {'1104139': [0, 0, 0, 0, 0, 0, 0],
				'1104138': [0, 0, 0, 0, 0, 0, 0],
				'1104161': [0, 0, 0, 0, 0, 0, 0],
				'1104152': [0, 0, 95975.0, 105080.0, 0, 0, 201055.0],
				'1104131': [0, 0, 0, 0, 0, 0, 0],
				'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104134': [0, 0, 0, 0, 0, 0, 0],
				'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104140': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104141': [0, 0, 0, 0, 0, 0, 0],
				'1104151': [0, 0, 0, 0, 0, 0, 0],
				'1104143': [0, 0, 0, 0, 0, 0, 0],
				'1104157': [0, 0, 0, 0, 0, 0, 0],
				'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104155': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104154': [0, 0, 0, 0, 0, 0, 0],
				'1104149': [0, 0, 0, 0, 0, 0, 0],
				'1104159': [0, 0, 0, 0, 0, 0, 0],
				'1104158': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104156': [0, 0, 0, 0, 0, 0, 0],
				'Total': [95617.5, 0, 95975.0, 315240.0, 206170.0, 0, 713002.5]},
		'test_WARateSC' : [0.02, None, 0.03, 0.043333333333333335,
				0.023125, None, 0.03256605867440858],
		}
