#!/usr/bin/python
from pprint import pprint
from LiqSpot import LiqEngine
import datetime

#TODO pilas los fondos de 4157 se van a negativo

eng = LiqEngine()

eng.setParameters(LSSpread = 1, PriorDayRateUsed = 3.5)

#TODO add MortgageOriginator
eng.setMortgageOriginator([u'ABCD', u'BCDE', u'EFGH', u'HIJK'])

eng.setLoans([{'loanAmount': 408378L, 'mortgageOriginator': u'HIJK', 'loanId': u'201144387'},
{'loanAmount': 360000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201144944'},
{'loanAmount': 260000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201145114'},
{'loanAmount': 625500L, 'mortgageOriginator': u'BCDE', 'loanId': u'201145234'},
{'loanAmount': 280000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201145359'},
{'loanAmount': 255000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201145735'},
{'loanAmount': 417000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201145759'},
{'loanAmount': 458000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201146570'},
{'loanAmount': 250000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201146741'},
{'loanAmount': 147250L, 'mortgageOriginator': u'BCDE', 'loanId': u'201147140'},
{'loanAmount': 478507L, 'mortgageOriginator': u'EFGH', 'loanId': u'201147282'},
{'loanAmount': 301000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201147471'},
{'loanAmount': 417000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201147482'},
{'loanAmount': 290700L, 'mortgageOriginator': u'BCDE', 'loanId': u'201147544'},
{'loanAmount': 314000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201147653'},
{'loanAmount': 327200L, 'mortgageOriginator': u'HIJK', 'loanId': u'201147776'},
{'loanAmount': 350000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201148009'},
{'loanAmount': 270000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201148154'},
{'loanAmount': 315500L, 'mortgageOriginator': u'ABCD', 'loanId': u'201148329'},
{'loanAmount': 228000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201148342'},
{'loanAmount': 152000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148353'},
{'loanAmount': 496000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201148440'},
{'loanAmount': 225500L, 'mortgageOriginator': u'ABCD', 'loanId': u'201148530'},
{'loanAmount': 350874L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148539'},
{'loanAmount': 256000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148544'},
{'loanAmount': 403000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201148589'},
{'loanAmount': 189000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148639'},
{'loanAmount': 295000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148780'},
{'loanAmount': 522269L, 'mortgageOriginator': u'HIJK', 'loanId': u'201148832'},
{'loanAmount': 228000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201148834'},
{'loanAmount': 241000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201148886'},
{'loanAmount': 40000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201148956'},
{'loanAmount': 260000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201148972'},
{'loanAmount': 504000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201148993'},
{'loanAmount': 198000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149047'},
{'loanAmount': 223000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149063'},
{'loanAmount': 220133L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149077'},
{'loanAmount': 268000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149154'},
{'loanAmount': 141000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149167'},
{'loanAmount': 85000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149168'},
{'loanAmount': 312000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149204'},
{'loanAmount': 393750L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149215'},
{'loanAmount': 258300L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149229'},
{'loanAmount': 294000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149241'},
{'loanAmount': 264000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149253'},
{'loanAmount': 175000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149257'},
{'loanAmount': 136451L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149269'},
{'loanAmount': 212000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149284'},
{'loanAmount': 330000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149289'},
{'loanAmount': 188000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149321'},
{'loanAmount': 96000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149336'},
{'loanAmount': 241800L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149359'},
{'loanAmount': 410000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149372'},
 {'loanAmount': 292575L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149374'},
 {'loanAmount': 178800L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149396'},
 {'loanAmount': 185000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149441'},
 {'loanAmount': 625500L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149444'},
 {'loanAmount': 172000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149456'},
 {'loanAmount': 485300L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149462'},
 {'loanAmount': 233000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149469'},
 {'loanAmount': 178500L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149471'},
 {'loanAmount': 304000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149474'},
 {'loanAmount': 584790L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149477'},
 {'loanAmount': 185000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149534'},
 {'loanAmount': 250000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149541'},
 {'loanAmount': 320000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149544'},
 {'loanAmount': 240000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149560'},
 {'loanAmount': 1250000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201149562'},
 {'loanAmount': 330000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149565'},
 {'loanAmount': 127000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149577'},
 {'loanAmount': 862500L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149578'},
 {'loanAmount': 1022000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201149579'},
 {'loanAmount': 267500L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149582'},
 {'loanAmount': 200000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149589'},
 {'loanAmount': 206000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149597'},
 {'loanAmount': 270500L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149622'},
 {'loanAmount': 248535L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149652'},
 {'loanAmount': 281673L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149664'},
 {'loanAmount': 504000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149669'},
 {'loanAmount': 402000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149687'},
 {'loanAmount': 616100L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149703'},
 {'loanAmount': 135200L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149712'},
 {'loanAmount': 290000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149733'},
 {'loanAmount': 417000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149741'},
 {'loanAmount': 801950L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149751'},
 {'loanAmount': 100000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149778'},
 {'loanAmount': 123000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149828'},
 {'loanAmount': 400000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149846'},
 {'loanAmount': 403500L, 'mortgageOriginator': u'HIJK', 'loanId': u'201149875'},
 {'loanAmount': 200900L, 'mortgageOriginator': u'HIJK', 'loanId': u'201149905'},
 {'loanAmount': 232000L, 'mortgageOriginator': u'ABCD', 'loanId': u'201149912'},
 {'loanAmount': 216000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149935'},
 {'loanAmount': 353471L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149940'},
 {'loanAmount': 100000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201149976'},
 {'loanAmount': 217000L, 'mortgageOriginator': u'BCDE', 'loanId': u'201149988'},
 {'loanAmount': 160000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201149991'},
 {'loanAmount': 230000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201150008'},
 {'loanAmount': 366000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201150040'},
 {'loanAmount': 166000L, 'mortgageOriginator': u'EFGH', 'loanId': u'201150096'},
 {'loanAmount': 394000L, 'mortgageOriginator': u'HIJK', 'loanId': u'201150125'}])

eng.setUsers([{'fundsAvailable': 598000.0, 'userId': u'1104131@test.com'},
 {'fundsAvailable': 418000.0, 'userId': u'1104133@test.com'},
 {'fundsAvailable': 187500.0, 'userId': u'1104134@test.com'},
 {'fundsAvailable': 860000.0, 'userId': u'1104136@test.com'},
 {'fundsAvailable': 300000.0, 'userId': u'1104138@test.com'},
 {'fundsAvailable': 250000.0, 'userId': u'1104139@test.com'},
 {'fundsAvailable': 74000.0, 'userId': u'1104140@test.com'},
 {'fundsAvailable': 285000.0, 'userId': u'1104141@test.com'},
 {'fundsAvailable': 500000.0, 'userId': u'1104143@test.com'},
 {'fundsAvailable': 752000.0, 'userId': u'1104145@test.com'},
 {'fundsAvailable': 47000.0, 'userId': u'1104149@test.com'},
 {'fundsAvailable': 283000.0, 'userId': u'1104151@test.com'},
 {'fundsAvailable': 1500000.0, 'userId': u'1104152@test.com'},
 {'fundsAvailable': 185000.0, 'userId': u'1104154@test.com'},
 {'fundsAvailable': 639000.0, 'userId': u'1104155@test.com'},
 {'fundsAvailable': 274000.0, 'userId': u'1104156@test.com'},
 {'fundsAvailable': 629000.0, 'userId': u'1104157@test.com'},
 {'fundsAvailable': 52000.0, 'userId': u'1104158@test.com'},
 {'fundsAvailable': 532000.0, 'userId': u'1104159@test.com'},
 {'fundsAvailable': 292000.0, 'userId': u'1104161@test.com'}])

eng.setBids([{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'loanId': u'201149669', 'userId': u'1104161@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'11:06:12 PM 1104161',
				'date': datetime.datetime(1900, 1, 1, 23, 6, 12),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'Specified', 'bidRate': 1.5, 'orderType':
				u'Competitive', 'loanId': u'201148329',
				'userId': u'1104145@test.com', 'orderTiming': u'Day Trade',
				'Aggregate': None, 'bidId': u'11:35:00 PM 1104145',
				'date': datetime.datetime(1900, 1, 1, 23, 35),
				'assetSubset': u'Loan', 'Participation': 10.0},
			{'bidType': u'Specified', 'bidRate': 4.0,
				'orderType': u'Competitive', 'loanId': u'201149669',
				'userId': u'1104133@test.com', 'orderTiming': u'Day Trade',
				'Aggregate': None, 'bidId': u'2:23:00 AM 1104133',
				'date': datetime.datetime(1900, 1, 1, 2, 23),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'loanId': u'201148440', 'userId': u'1104149@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'2:27:48 AM 1104149',
				'date': datetime.datetime(1900, 1, 1, 2, 27, 48),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'General', 'orderType': u'Noncompetitive',
				'userId': u'1104134@test.com', 'Aggregate': 15000000.0,
				'bidId': u'3:00:00 PM 1104134',
				'date': datetime.datetime(1900, 1, 1, 15, 0),
				'orderTiming': u'Auto', 'Participation': 10.0},
			{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'userId': u'1104143@test.com', 'orderTiming': u'Auto',
				'Aggregate': None, 'mortgageOriginator': u'ABCD',
				'bidId': u'3:00:00 PM 1104143',
				'date': datetime.datetime(1900, 1, 1, 15, 0),
				'assetSubset': u'MO', 'Participation': 20.0},
			{'bidType': u'Specified', 'bidRate': 3.0,
				'orderType': u'Competitive', 'userId': u'1104152@test.com',
				'orderTiming': u'Auto', 'Aggregate': None,
				'mortgageOriginator': u'BCDE',
				'bidId': u'3:00:00 PM 1104152',
				'date': datetime.datetime(1900, 1, 1, 15, 0),
				'assetSubset': u'MO', 'Participation': 20.0},
			{'bidType': u'General', 'bidRate': 3.0,
				'orderType': u'Competitive', 'userId': u'1104154@test.com',
				'Aggregate': 20000000.0, 'bidId': u'3:00:00 PM 1104154',
				'date': datetime.datetime(1900, 1, 1, 15, 0),
				'orderTiming': u'Auto', 'Participation': 20.0},
			{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'loanId': u'201148329', 'userId': u'1104151@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'3:54:12 AM 1104151',
				'date': datetime.datetime(1900, 1, 1, 3, 54, 12),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'General', 'orderType': u'Noncompetitive',
				'userId': u'1104131@test.com', 'Aggregate': 1000000.0,
				'bidId': u'4:37:24 AM 1104131',
				'date': datetime.datetime(1900, 1, 1, 4, 37, 24),
				'orderTiming': u'Day Trade', 'Participation': 50.0},
			{'bidType': u'Specified', 'bidRate': 6.0, 'orderType': u'Competitive',
				'loanId': u'201149669', 'userId': u'1104136@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'5:06:12 PM 1104136',
				'date': datetime.datetime(1900, 1, 1, 17, 6, 12),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'General', 'bidRate': 2.125, 'orderType': u'Competitive',
				'userId': u'1104138@test.com', 'Aggregate': 1000000.0,
				'bidId': u'6:32:36 PM 1104138',
				'date': datetime.datetime(1900, 1, 1, 18, 32, 36),
				'orderTiming': u'Day Trade', 'Participation': 50.0},
			{'bidType': u'Specified', 'bidRate': 2.125, 'orderType': u'Competitive',
				'userId': u'1104155@test.com', 'orderTiming': u'Day Trade',
				'Aggregate': None, 'mortgageOriginator': u'EFGH',
				'bidId': u'6:47:00 AM 1104155',
				'date': datetime.datetime(1900, 1, 1, 6, 47),
				'assetSubset': u'MO', 'Participation': 20.0},
			{'bidType': u'General', 'bidRate': 2.25, 'orderType': u'Competitive',
				'userId': u'1104139@test.com', 'Aggregate': 500000.0,
				'bidId': u'7:15:48 PM 1104139',
				'date': datetime.datetime(1900, 1, 1, 19, 15, 48),
				'orderTiming': u'Day Trade', 'Participation': 30.0},
			{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'loanId': u'201148009', 'userId': u'1104156@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'7:30:12 AM 1104156',
				'date': datetime.datetime(1900, 1, 1, 7, 30, 12),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'Specified', 'bidRate': 2.5,
				'orderType': u'Competitive', 'loanId': u'201148440',
				'userId': u'1104140@test.com', 'orderTiming': u'Day Trade',
				'Aggregate': None, 'bidId': u'7:59:00 PM 1104140',
				'date': datetime.datetime(1900, 1, 1, 19, 59),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'General', 'orderType': u'Noncompetitive',
				'userId': u'1104157@test.com', 'Aggregate': 1000000.0,
				'bidId': u'8:13:24 AM 1104157',
				'date': datetime.datetime(1900, 1, 1, 8, 13, 24),
				'orderTiming': u'Day Trade', 'Participation': 30.0},
			{'bidType': u'General', 'bidRate': 2.5, 'orderType': u'Competitive',
				'userId': u'1104141@test.com', 'Aggregate': 500000.0,
				'bidId': u'8:42:12 PM 1104141',
				'date': datetime.datetime(1900, 1, 1, 20, 42, 12),
				'orderTiming': u'Day Trade', 'Participation': 20.0},
			{'bidType':	u'Specified', 'bidRate': 2.25, 'orderType': u'Competitive',
				'loanId': u'201148329', 'userId': u'1104158@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'8:56:36 AM 1104158',
				'date': datetime.datetime(1900, 1, 1, 8, 56, 36),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'Specified', 'orderType': u'Noncompetitive',
				'loanId': u'201148329', 'userId': u'1104159@test.com',
				'orderTiming': u'Day Trade', 'Aggregate': None,
				'bidId': u'9:39:48 PM 1104159',
				'date': datetime.datetime(1900, 1, 1, 21, 39, 48),
				'assetSubset': u'Loan', 'Participation': 20.0},
			{'bidType': u'Specified', 'bidRate': 7.0, 'orderType':
				u'Competitive', 'loanId': u'201145114',
				'userId': u'1104158@test.com', 'orderTiming': u'Day Trade',
				'Aggregate': None,
				'bidId': u'1104158@test.com 2012-06-06 21:15:55.614542',
				'date': datetime.datetime(2012, 6, 6, 21, 15, 55, 614542),
				'assetSubset': u'Loan', 'Participation': 5.0}
			])

eng.Calc()
pprint(eng.Data)
