import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids8.csv', '-l', '../../sample/loans8.csv',
		'-d', ',', '-M', '../mo.csv', '-o', 'test.csv', '-r', '-A', '-R', 3.5]

scenario = {'test_Summary' : {'1104139': [1932.7408020093592, 18225.15907325465,
							0.0, 22302.091526017794, 28129.72421642816,
							29410.284382290036, 100000.0],
						'1104138': [0, 0, 0, 0, 51542.5, 0, 51542.5],
						'1104161': [1932.7408020093592, 18225.15907325465, 0.0,
							22302.091526017794, 28129.72421642816, 29410.284382290036,
							100000.0],
						'1104152': [0, 0, 143962.5, 0, 0, 0, 143962.5],
						'1104131': [0, 0, 143962.5, 157620.0, 0, 0, 301582.5],
						'1104133': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
						'1104134': [2881.387969859613, 27170.613901180233, 0.0,
							33248.627109733105, 41936.63675357759, 43845.73426564946,
							149083.0],
						'1104136': [9663.704010046797, 91125.79536627326, 0.0,
							111510.45763008896, 140648.6210821408, 147051.4219114502,
							500000.0],
						'1104140': [63745.0, 75137.0, 0, 0, 0, 0, 138882.0],
						'1104141': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
						'1104151': [1932.7408020093592, 18225.15907325465, 0.0,
							22302.091526017794, 28129.72421642816, 29410.284382290036,
							100000.0],
						'1104143': [63745.0, 0, 0, 0, 0, 0, 63745.0],
						'1104157': [1932.7408020093592, 18225.15907325465, 0.0,
							22302.091526017794, 28129.72421642816, 29410.284382290036,
							100000.0],
						'1104145': [95617.5, 0, 0, 0, 0, 0, 95617.5],
						'1104155': [9663.704010046797, 91125.79536627326, 0.0,
							111510.45763008896, 140648.6210821408, 147051.4219114502,
							500000.0],
						'1104154': [1932.7408020093592, 18225.15907325465, 0.0,
							22302.091526017794, 28129.72421642816, 29410.284382290036,
							100000.0],
						'1104149': [31872.5, 0, 0, 0, 0, 0, 31872.5],
						'1104159': [0, 0, 143962.5, 0, 0, 0, 143962.5],
						'1104158': [0, 0, 47987.5, 0, 0, 0, 47987.5],
						'1104156': [31872.5, 0, 0, 0, 0, 0, 31872.5],
						'Total': [318725.0, 375685.00000000006, 479875.0, 525400.0,
							515425.0000000001, 485000.0, 2700110.0]},
		'test_SumRateAllocation' : {'1104139': 0.026202260491677436, '1104138': 0.02625,
						'1104161': 0.02870226049167744, '1104152': 0.025,
						'1104131': 0.025, '1104133': 0, '1104134': 0.03370226049167744,
						'1104136': 0.031202260491677437, '1104140': 0.02875, '1104141': 0,
						'1104151': 0.02495226049167744, '1104143': 0.02875,
						'1104157': 0.023702260491677438, '1104145': 0.02375,
						'1104155': 0.03245226049167744, '1104154': 0.023702260491677438,
						'1104149': 0.03375, '1104159': 0.03125, '1104158': 0.02125,
						'1104156': 0.025}
		}
