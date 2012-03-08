import datetime

argument = ['LiqSpot.py', '-b', '../../sample/bids7.csv', '-l', '../../sample/loans7.csv',
		'-d', ',', '-M', '../mo.csv', '-o', 'test.csv', '-R', 3.5]

scenario = {'test_Summary' : {'1104139': [11804.14871986697, 13913.692405124235,
						17772.42408642611, 19458.46650692009, 19089.03711330279,
						17962.23116835981, 100000.0],
					'1104138': [15120.786008793746, 17823.052762455653, 22765.980660349516,
						24925.754079599134, 24452.525307341803, 23009.118250105785,
						128097.21706864564],
					'1104161': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104152': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104131': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104133': [21068.29517225262, 24833.453515688212, 31720.59972008699,
						34729.88401757479, 34070.518594896246, 32059.371428480725,
						178482.1224489796],
					'1104134': [9450.49125549609, 11139.407976534783, 14228.737912718447,
						15578.596299749457, 15282.828317088628, 14380.698906316115,
						80060.76066790352],
					'1104136': [43346.25322520873, 51092.75125237287, 65262.477893001946,
						71453.82836151753, 70097.23921437985, 65959.47231696991,
						367212.0222634509],
					'1104140': [8735.070052701556, 10296.132379791934, 13151.59382395532,
						14399.265215120866, 14125.887463844065, 13292.051064586258, 74000.0],
					'1104141': [14364.746708354058, 16931.90012433287, 21627.68162733204,
						23679.466375619177, 23229.899041974713, 21858.662337600494,
						121692.35621521334],
					'1104151': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104143': [25201.310014656243, 29705.08793742609, 37943.301100582525,
						41542.92346599856, 40754.20884556967, 38348.53041684297,
						213495.36178107606],
					'1104157': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104145': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104155': [32207.27419873068, 37963.10238403054, 48491.53880654447,
						53091.85618954616, 52083.87890463805, 49009.421872725325,
						272847.0723562152],
					'1104154': [11804.14871986697, 13913.692405124235, 17772.42408642611,
						19458.46650692009, 19089.03711330279, 17962.23116835981, 100000.0],
					'1104149': [2368.9231413776865, 2792.278266118052, 3566.670303454757,
						3905.034805803864, 3830.895631483549, 3604.7618591832393,
						20068.564007421148],
					'1104159': [26814.193855594243, 31606.21356542136, 40371.6723710198,
						44201.67056782247, 43362.47821168614, 40802.836363520924,
						227159.06493506493],
					'1104158': [11804.14871986697, 13913.692405124235,
						17772.42408642611, 19458.46650692009, 19089.03711330279,
						17962.23116835981, 100000.0],
					'1104156': [13810.31788803162, 16278.388189709498, 20792.92900311922,
							22765.52205936721, 22333.306447372182, 21014.99466842995,
							116995.45825602967],
					'Total': [318725.0, 375684.99999999994, 479874.99999999994,
						525400.0000000001, 515425.0, 485000.0,
						2700109.9999999995]},
		'test_SumRateAllocation' : {'1104139': 0.0575, '1104138': 0.05810318275154005,
				'1104161': 0.060000000000000005, '1104152': 0.060000000000000005,
				'1104131': 0.060000000000000005, '1104133': 0.05810318275154005,
				'1104134': 0.05810318275154005, '1104136': 0.05810318275154005,
				'1104140': 0.06375, '1104141': 0.05810318275154005,
				'1104151': 0.05625000000000001, '1104143': 0.05810318275154005,
				'1104157': 0.05500000000000001, '1104145': 0.058750000000000004,
				'1104155': 0.05810318275154005, '1104154': 0.05500000000000001,
				'1104149': 0.05810318275154005, '1104159': 0.05810318275154005,
				'1104158': 0.05625000000000001, '1104156': 0.05810318275154005}
		}
