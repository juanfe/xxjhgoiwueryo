import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids2.csv',
		'-u', '../../sample/users2.csv', '-l', '../../sample/loans2.csv',
		'-d', ',', '-M', '../mo.csv', '-o', 'test.csv', '-R', 3.5]

scenario = { 'test_Summary' : {'1104139': [0, 0, 0, 0, 0, 0, 0],
				'1104138': [0, 0, 0, 0, 0, 0, 0],
				'1104161': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104152': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104131': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104134': [0, 0, 0, 0, 0, 0, 0],
				'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104140': [0, 0, 0, 0, 0, 0, 0],
				'1104141': [0, 0, 0, 0, 0, 0, 0],
				'1104151': [0, 0, 0, 0, 0, 0, 0],
				'1104143': [0, 0, 0, 0, 0, 0, 0],
				'1104157': [0, 0, 0, 0, 0, 0, 0],
				'1104145': [0, 0, 0, 0, 0, 0, 0],
				'1104155': [0, 0, 0, 0, 0, 0, 0],
				'1104154': [0, 0, 0, 0, 0, 0, 0],
				'1104149': [0, 0, 0, 0, 0, 0, 0],
				'1104159': [0, 0, 0, 0, 0, 0, 0],
				'1104158': [0, 0, 0, 0, 0, 0, 0],
				'1104156': [0, 0, 0, 0, 0, 0, 0],
				'Total': [0, 0, 0, 525400.0, 0, 0, 525400.0]},
		'test_SumRateAllocation' :
			{'1104139': 0, '1104138': 0, '1104161': 0.035, '1104152': 0.035,
				'1104131': 0.035, '1104133': 0.035, '1104134': 0,
				'1104136': 0.035, '1104140': 0, '1104141': 0, '1104151': 0,
				'1104143': 0, '1104157': 0, '1104145': 0, '1104155': 0,
				'1104154': 0, '1104149': 0, '1104159': 0, '1104158': 0,
				'1104156': 0}
		}
