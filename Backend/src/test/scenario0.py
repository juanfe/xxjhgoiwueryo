import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids0.csv',
		'-u', '../../sample/users0.csv', '-l', '../../sample/loans0.csv',
		'-d', ';', '-M', '../mo.csv', '-o', 'test.csv', '-R', 1]

scenario = {'test_init' : '../mo.csv', 
		'test_LoadMortgageOperators' :
			['ABC Mortgage', 'Prime Lending', 'Best Loans Inc', 'Integrity Lending'],
		'test_addLoans' : { 'p' : ['MO', 'Load Amount', 'Rate'],
			'q' : ['ABC Mortgage', ' 318725', '0.01'],
			'r' : [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.01}],
			},
		'test_LoadLoans' : 
			[{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.01},
				{'MO': 'ABC Mortgage', 'Load Amount': 375685.0, 'Rate': 0.01},
				{'MO': 'Prime Lending', 'Load Amount': 479875.0, 'Rate': 0.01},
				{'MO': 'Prime Lending', 'Load Amount': 525400.0, 'Rate': 0.01},
				{'MO': 'Best Loans Inc', 'Load Amount': 515425.0, 'Rate': 0.01},
				{'MO': 'Integrity Lending', 'Load Amount': 485000.0, 'Rate': 0.01},
				{'MO': 'Total', 'Load Amount': 2700110.0}],
		'test_LoadBids' : { 'p' : 20,
			'q' : '1104154',
			'r' : {'loannum': '',
				'dateorder': datetime.datetime(2012, 1, 5, 9, 16), 'userid': '1104154@test.com',
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
		'test_CalcRemaing' : [(223107.5, 'under'), (375685.0, 'under'),
				(383900.0, 'under'), (210160.0, 'under'), (309255.0, 'under'),
				(485000.0, 'under'), (1987107.5, 'under')],
		'test_WARateSNC' : [0.0225, 0.0225, 0.03, 0.06, 0.025, 0.06,
				0.03013764067429058],
		'test_WARateS' : { 'p': [0.021666666666666667, 0.0225, 0.03, 0.0475, 0.02375,
				0, 0.03150890885353453],
				'q': {'1104139': {'aggregate': 250000.0, 'v0': 0,
						'allocated': 250000.0, 'bidrate': 0.0225, 'rank': 3},
					'1104138': {'aggregate': 300000.0, 'v0': 0, 'allocated': 300000.0,
						'bidrate': 0.02125, 'rank': 4},
					'1104154': {'aggregate': 185000.0, 'v0': 0, 'allocated': 185000.0,
						'bidrate': 0.03, 'rank': 1},
					'Total': {'aggregate': 1020000.0, 'allocated': 1020000.0,
						'bidrate': 0.024191176470588237},
					'1104141': {'aggregate': 285000.0, 'v0': 0, 'allocated': 285000.0,
						'bidrate': 0.025, 'rank': 2}}
				},
		'test_CalcRateAwarded' : {'1104139': {'rateawarded': 0.038617011249892495, 'rate': 0.0225},
				'1104138': {'rateawarded': 0.037367011249892494, 'rate': 0.02125},
				'1104141': {'rateawarded': 0.0411170112498925, 'rate': 0.025},
				'1104154': {'rateawarded': 0.046117011249892495, 'rate': 0.03},
				'Total': {'rateawarded': 0.040308187720480726}},
		'test_WARateTot' : [0.021919117647058825, 0.023514705882352945,
				0.043587239510208486, 0.04500070978502713,
				0.023926470588235292, 0.05268226761705371,
				0.036193302533492205],
		'test_Summary' : {'1104139': [5543.299916135251, 39203.726641962916,
					66768.3061512063, 18275.628055141333, 35857.31096429852,
					84351.72827125568, 250000.0],
				'1104138': [6651.959899362301, 47044.471970355495, 80121.96738144755,
					21930.7536661696, 43028.773157158226, 101222.07392550682, 300000.0],
				'1104161': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104152': [0, 0, 95975.0, 105080.0, 0, 0, 201055.0],
				'1104131': [3913.036502380041, 27674.05980196056, 47132.00135739895, 12900.83538066028,
					25311.812242393706, 59544.20593471866, 176475.9512195122],
				'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104134': [1226.9136190572872, 8677.067245598002, 14778.010459050674,
					4044.994371026426, 7936.395979011404, 18669.797011303926,
					55333.17868504772],
				'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104140': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104141': [6319.361904394186, 44692.248371837726, 76115.86901237519,
					20834.21598286112, 40877.33449930031, 96160.97022923148, 285000.0],
				'1104151': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104143': [63745.0, 75137.0, 0, 0, 0, 0, 138882.0],
				'1104157': [4115.886220730846, 29108.668253232765, 49575.299086628664,
					13569.60778333665, 26623.96304425692, 62630.94570725424,
					185624.3700954401],
				'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104155': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104154': [4102.0419379400855, 29010.757715052558, 49408.546551892665,
					13523.964760804587, 26534.410113580907, 62420.2789207292, 185000.0],
				'1104149': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104159': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104158': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104156': [0, 75137.0, 0, 0, 0, 0, 75137.0],
				'Total': [318725.0, 375685.00000000006, 479874.99999999994, 525400.0,
					515425.0, 485000.0, 2700110.0]},
		'test_SumRateAllocation' : {'1104139': 0.038617011249892495,
				'1104138': 0.037367011249892494, '1104161': 0.060000000000000005,
				'1104152': 0.03, '1104131': 0.04030818772048073, '1104133': 0.04,
				'1104134': 0.04030818772048073, '1104136': 0.06, '1104140': 0.025,
				'1104141': 0.0411170112498925, '1104151': 0.0225,
				'1104143': 0.022500000000000003, '1104157': 0.04030818772048073,
				'1104145': 0.015, '1104155': 0.02125,
				'1104154': 0.046117011249892495, '1104149': 0.025, '1104159': 0.0225,
				'1104158': 0.0225, '1104156': 0.0225},
		}
