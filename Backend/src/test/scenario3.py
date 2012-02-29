import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids3.csv', '-l', '../../sample/loans3.csv',
		'-d', ',', '-M', '../mo.csv', '-o', 'test.csv', '-r', '-A']

scenario = { 'test_Summary' : {'1104139': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104138': [35412.446159600906, 41741.07721537271,
					53317.272259278325, 58375.399520760264, 57267.11133990838,
					53886.69350507942, 300000.0],
				'1104158': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104141': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104131': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104133': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104134': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104136': [101515.67899085593, 119657.75468406842,
					152842.84714326455, 167342.81195951276, 164165.71917440402,
					154475.18804789433, 860000.0],
				'1104140': [8735.070052701556, 10296.132379791934, 13151.59382395532,
					14399.265215120866, 14125.887463844065, 13292.051064586258,
					74000.0],
				'1104152': [23857.36497772313, 28120.96371999659, 35919.846321075805,
					39327.50665713619, 38580.852909696274, 36303.465414372,
					202110.00000000003],
				'1104151': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104143': [59020.74359933484, 69568.46202562118, 88862.12043213054,
					97292.33253460044, 95445.18556651396, 89811.15584179903,
					500000.00000000006],
				'1104157': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104145': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104155': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104154': [21837.67513175389, 25740.330949479838, 32878.984559888304,
					35998.163037802165, 35314.71865961017, 33230.127661465645,
					185000.00000000003],
				'1104149': [5547.949898337475, 6539.435430408391, 8353.039320620272,
					9145.479258252442, 8971.847443252313, 8442.24864912911,
					47000.0],
				'1104159': [62798.07118969227, 74020.84359526093, 94549.2961397869,
					103519.04181681488, 101553.67744277084, 95559.06981567417,
					532000.0],
				'1104161': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'1104156': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				'Total':  [318725.0, 375685.0, 479875.00000000006, 525400.0,
					515425.00000000006, 485000.0, 2700110.0]},
		'test_SumRateAllocation' :
			{'1104139': 0.03125, '1104138': 0.07625000000000001,
				'1104161': 0.04375, '1104152': 0.07875, '1104131': 0.04625,
				'1104133': 0.0375, '1104134': 0.04, '1104136': 0.07750000000000001,
				'1104140': 0.07125000000000001, '1104141': 0.0325,
				'1104151': 0.03125, '1104143': 0.075, '1104157': 0.0325,
				'1104145': 0.04875, '1104155': 0.03375, '1104154': 0.07125,
				'1104149': 0.07250000000000001, '1104159': 0.07625000000000001,
				'1104158': 0.0325, '1104156': 0.03375}
		}
