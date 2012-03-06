import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids6.csv', '-l', '../../sample/loans6.csv',
		'-d', ',', '-M', '../mo.csv', '-o', 'test.csv']

scenario = {'test_Summary' : {'1104139': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104138': [0, 0, 0, 0, 0, 0, 0],
				'1104161': [0, 0, 47987.5, 0, 0, 0, 47987.5],
				'1104152': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104131': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104133': [0, 0, 143962.5, 0, 0, 0, 143962.5],
				'1104134': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104136': [0, 0, 0, 0, 0, 0, 0],
				'1104140': [0, 0, 95975.0, 0, 0, 0, 95975.0],
				'1104141': [95617.5, 0, 0, 0, 0, 0, 95617.5],
				'1104151': [0, 0, 0, 0, 0, 0, 0],
				'1104143': [0, 0, 0, 0, 0, 0, 0],
				'1104157': [0, 0, 47987.5, 0, 0, 0, 47987.5],
				'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104155': [0, 0, 0, 0, 0, 0, 0],
				'1104154': [0, 0, 0, 0, 0, 0, 0],
				'1104149': [0, 0, 95975.0, 0, 0, 0, 95975.0],
				'1104159': [0, 0, 0, 0, 0, 0, 0],
				'1104158': [0, 0, 0, 0, 0, 0, 0],
				'1104156': [0, 0, 47987.5, 0, 0, 0, 47987.5],
				'Total': [318725.0, 0, 479875.0, 0, 0, 0, 798600.0]},
		'test_SumRateAllocation' :
			{'1104139': 0.0225, '1104138': 0, '1104161': 0.025, '1104152': 0.025,
				'1104131': 0.025, '1104133': 0.035, '1104134': 0.035, '1104136': 0,
				'1104140': 0.02875, '1104141': 0.035, '1104151': 0, '1104143': 0,
				'1104157': 0.02, '1104145': 0.02375, '1104155': 0, '1104154': 0,
				'1104149': 0.035, '1104159': 0, '1104158': 0, '1104156': 0.035}
		}