#!/usr/bin/python

import csv, sys, os
from optparse import OptionParser
from datetime import datetime
from copy import deepcopy

class LiqEngine:
	def __init__(self):
		self.Mo = []
		self.Loans = []
		self.TotalLoans = 0
		self.Users = {}
		self.Bids = {}
		self.Exceptions = []
		parser = self.ParseArg()
		(self.options, args) = parser.parse_args()
		return

	def ParseArg(self):
		parser = OptionParser()
	
		parser.add_option("-b", "--bids", dest="bidsFileName",
				help="Read the bids information.", metavar="BIDSFILE")
		parser.add_option("-u", "--users", dest="usersFileName",
				help="List of users associated in case of a json bid file")
		parser.add_option("-l", "--loans", dest="loansFilename",
				help="Read the loan or mortgages information", metavar="LOANFILE")
		#TODO enable exceptions
		parser.add_option("-e", "--exceptions", dest="exceptions",
				help="List of exceptions in the calculation of the assets.",
				metavar="EXCEPTIONSFILE", default = False)
		parser.add_option("-o", "--output", dest="output",
				help="Write the Liquidity Spots for the Loans",
				metavar="OUTFILE", default = False)
		parser.add_option("-d", "--delimiter", dest="delimiter",
				help="Assigne delimiter to use in the csv format, default is ','.",
				default=',')
		parser.add_option("-v", "--verbose", dest="Verbose", action="store_true",
				help="Verbose mode",
				default=False)
		parser.add_option("-M", "--MorgageOperators", dest="OperatorFilename",
				default= os.path.dirname(sys.argv[0])+"/mo.csv",
				help = "Specify the Mortgage Operators, default mo.csv")
		parser.add_option("-r", "--rankinvert", dest="rank_invert",
				action="store_true",
				help="Inverte the order of the order of the rank in " +
				"General/Competitive bids.", default = False)
		parser.add_option("-A", "--allocacceptexcetion",
				dest="AllocAcceptException", action="store_true",
				help="Excetion in the calculation of Allocate and Accepted " +
				"in General/Competitive bids.", default = False)
		parser.add_option("-R", "--priordayrateused", dest="PriorRate",
				default= 0, help="Prior day rate used in the Specified/Non " +
				"Comptetitive bids")
		parser.usage = "usage: %prog [options arg] [-v]"
		return parser
	
	def addLoans(self, idl, lo):
		d = dict(zip(idl, lo))
		
		try:
			self.Mo.index(d["MO"])
		except:
			try:
				sys.exit('The mortgage "%s", does not match %s.' % (d["MO"], self.options.OperatorFilename))
			except:
				sys.exit('Error: in the file %s, see the field delimiter in csv file, look "LiqSpot.py --help".'
						% self.options.loansFilename)
		try:
			d['Load Amount'] = float(d['Load Amount'].strip(' '))
			d['Rate'] = float(d['Rate'].strip(' '))
		except:
			sys.exit("Error: The number's format have an error, it is " +
					"possible that you are using the same ',' separator of " +
					"field and decimal expressions. Use '.' as decimal " +
					"separator!")
		self.TotalLoans = self.TotalLoans + d['Load Amount']
		self.Loans.append(d)

	def addLoansJson(self, k, lo):
		#TODO add LoansJson
		d = {}

	def LoadMortgageOperators(self):
		fmo = csv.reader(open(self.options.OperatorFilename, "rb"),
			delimiter=self.options.delimiter, quoting=csv.QUOTE_NONE)
		
		try:
			for op in fmo:
				if (op[0] != "Name"):

					self.Mo.append(op[0])
		except csv.Error, e:
			sys.exit('File %s, line %d: %s' % (self.options.OperatorFilename, fmo.line_num, e)) 
	
	def setMortgageOperators(self, Mo):
		self.Mo = Mo

	def LoadLoans(self):
		fileName, fileExt = os.path.splitext(self.options.loansFilename)
		if fileExt.lower() == ".json":
			try:
				flo = json.loads(open(self.options.loansFilename, "rb").read())
			except:
				sys.exit('There are no parameter -l for the loan file name.')

			#try:
			for k, lo in flo.iteritems():
				self.addLoansJson(k, lo)
			self.Loans.append({'MO': 'Total', 'Load Amount': self.TotalLoans})
			#except:
			#	sys.exit('File %s, line %d: %s' % (self.options.loansFilename, flo.line_num, e))
		else:
			try:
				flo = csv.reader(open(self.options.loansFilename, "rb"),
					delimiter=self.options.delimiter,quoting=csv.QUOTE_NONE)
			except:
				sys.exit('There are no parameter -l for the loan file name.')
		
			try:
				idlo = flo.next()
				idlo.append("Rate")
				for lo in flo:
					lo.append(str(float(self.options.PriorRate)/100))
					self.addLoans(idlo, lo)
				self.Loans.append({'MO': 'Total', 'Load Amount': self.TotalLoans})
			except csv.Error, e:
				sys.exit('File %s, line %d: %s' % (self.options.loansFilename, flo.line_num, e))

	def setLoans(self, Lo):
		try:
			tot =  0
			self.LoanIndex = []
			for l in Lo:
				tot += l['Load Amount']
				l['Rate'] = 0
				self.LoanIndex.append(l['Loand Id'])
				del(l['Loand Id'])
				l['MO'] = l['Mortgage Operator']
				del(l['Mortgage Operator'])
			Lo.append({'MO': 'Total', 'Load Amount': tot})
			self.Loans = Lo
		except:
			sys.exit('There are an error in %s'%(Lo))

	def checkUsersColNames(self, iduser):
		duser = {"userid":"userid",
				"funds available":"funds"}
		for u in iduser:
			try:
				p = iduser.index(u)
				iduser[p] = duser[u.lower()]	
			except:
				sys.exit('The column %s does not match witch the format' % (u) )


	def checkBidsColNames(self, idbid):
		dbid = {"time":"time",
				"bidid":"id",
				"bid type":"specified",
				"if general: aggregate $":"aggregate",
				"if general, max % per asset".lower():"genrate",
				"if specified, bid %":"sperate",
				"if specified, loan or mo":"lorm",
				"loan # if applicable":"loannum",
				"mo if applicable":"mo",
				"order type":"competitive",
				"if competitive, bid rate":"bidrate",
				"userid":"userid",
				"if auto, date/time order placed":"dateorder",
				"id":"id",
				"type":"specified",
				"aggregate $":"aggregate",
				"genrate":"genrate",
				"sperate":"sperate",
				"lorm":"lorm",
				"loannum":"loannum",
				"mo":"mo",
				"competitive":"competitive",
				"bidrate":"bidrate",
				"order timing":"ordertiming",
				"funds":"funds",
				"dateorder":"dateorder"}

		for d in idbid:
			try:
				p = idbid.index(d)
				idbid[p] = dbid[d.lower()]	
			except:
				sys.exit('The column %s does not match witch the format' % (d) )

	def PriceToFloat(self, val):
		try:
			return val if val == '' else float(val.strip('$ ').replace(',',''))
		except:
			sys.exit("Error: The number's format have an error, it is " +
					"possible that you are using the same ',' separator of " +
					"field and decimal expressions. Use '.' as decimal " +
					"separator!")

	def RateToFloat(self, val):
		try:
			return val if val == '' else float(val.strip('% '))/100
		except:
			sys.exit("Error: The number's format have an error, it is " +
					"possible that you are using the same ',' separator of " +
					"field and decimal expressions. Use '.' as decimal " +
					"separator!")

	def cleanUserData(self, duser):
		duser['funds'] = self.PriceToFloat(duser['funds'])
	
	def cleanBidData(self, dbid):
		dbid['aggregate'] = self.PriceToFloat(dbid['aggregate'])
		rates = ['genrate','sperate', 'bidrate']
		for r in rates:
			dbid[r] = self.RateToFloat(dbid[r])
		if dbid['competitive'] == 'Competitive':
			dbid['competitive'] = True
		else:
			dbid['competitive'] = False

		if dbid['specified'] == 'Specified':
			dbid['specified'] = True
		else:
			dbid['specified'] = False

		#TODO add today or the file date to the date
		dbid['time'] = datetime.strptime(dbid['time'], '%I:%M:%S %p')
		if dbid['dateorder'] != '':
			dbid['dateorder'] = datetime.strptime(dbid['dateorder'], '%m/%d/%y %I:%M %p')

	def addUsers(self, iduser, u):
		duser = dict(zip(iduser, u))
		id = duser['userid']
		del(duser['userid'])
		self.cleanUserData(duser)
		self.Users[id] = duser

	def addBids(self, idbid, b):
		dbid = dict(zip(idbid, b))
		id = dbid["id"]
		del(dbid["id"])
		self.cleanBidData(dbid)
		self.Bids[id] = dbid

	def LoadUsers(self):
		try:
			fusers = csv.reader(open(self.options.usersFileName, "rb"),
				delimiter=self.options.delimiter)
		except:
			sys.exit('There are no parameter -u for the user file name, or the file format is incorrect.')
		
		try:
			iduser = fusers.next()
			self.checkUsersColNames(iduser)
			for u in fusers:
				self.addUsers(iduser, u)
		except csv.Error, e:
			sys.exit('File %s, line %d: %s' % (self.options.usersFileName, fusers.line_num, e))

	def setUsers(self, Users):
		try:
			for u in Users:
				self.Users[u['User Id']] = {'funds': u['Funds available']} 
		except:
			 sys.exit('Users format error in %s'%(Users))

	def LoadBids(self):
		fileName, fileExt = os.path.splitext(self.options.bidsFileName)
		if fileExt.lower() == ".json":
			try:
				jsonbids = json.loads(open(self.options.bidsFileName, "rb").read())
			except:
				sys.exit('There are no parameter -l for the loan file name.')

			#try:
			for k, jbit in jsonbids.iteritems():
				self.addBidsJson(k, jbit)
			self.Loans.append({'MO': 'Total', 'Load Amount': self.TotalLoans})
		else:
			try:
				fbids = csv.reader(open(self.options.bidsFileName, "rb"),
					delimiter=self.options.delimiter)
			except:
				sys.exit('There are no parameter -b for the bids file name, or the file format is incorrect.')
		
			try:
				idbid = fbids.next()
				self.checkBidsColNames(idbid)
				for b in fbids:
					self.addBids(idbid, b)
			except csv.Error, e:
				sys.exit('File %s, line %d: %s' % (self.options.bidsFileName, fbids.line_num, e))

	def checkExceptionsColNames(self, iexc):
		exc = {"Bid ID": "id",
				"Loan Number": "loan",
				"Specified" : "specified",
				"Competitive" : "competitive",
				"Allocate" : "allocate",
				"Comment" : "comment"}

		for e in iexc:
			try:
				p = iexc.index(e)
				iexc[p] = exc[d.lower()]
			except:
				sys.exit('The column %s does not match witch the format' % (d))

	def cleanExceptionData(self, excep):
		excep['allocate'] = this.PriceToFloat(excep['allocate'])

	def addException(self, headexc, ex):
		excep = dict(zip(headexc, ex))
		id = excep["Bid ID"]
		del(excep["Bid ID"])
		self.cleanExceptionData(excep)
		self.Exceptions[id] = excep

	def LoadExceptions(self):
		if not self.options.exceptions:
			return None
		try:
			fexceptions = csv.reader(open(self.options.exceptions, "rb"),
					delimiter=self.options.delimiter)
		except:
			sys.exit('There are problems with file %s.' % (self.options.exceptions)) 

		try:
			headexc = fexceptions.next()
			self.checkExceptionsColNames(exc)
			for b in fexceptions:
				self.addException(headexc, b)
		except csv.Error, e:
			sys.exit('File %s, line %d: %s' % (self.options.exceptions,
				fexceptions.line_num, e))

	def SpecifiedCompetitive(self, bid, specified, competitive):
		return self.Bids[bid]['specified'] == specified and self.Bids[bid]['competitive'] == competitive

	def RankRateGenericCompetitive(self, Specified = False, Competitive = True):
		R = [] 
		for k, bid in self.Bids.iteritems():
			if self.SpecifiedCompetitive(k, Specified, Competitive):
				if (bid['bidrate'] > 0):
					R.append({'id':k, 'time':bid['time'], 'bidrate':bid['bidrate']})
		R = sorted(R, key = lambda l: (l['bidrate'], l['time']),
				reverse=not self.options.rank_invert)
		rank = {}
		i = 1
		for r in R:
			rank[r['id']] = i
			i = i + 1
		return rank

	def SpecifiedAssetAssignation(self, Competitive):
		if self.options.Verbose:
			print "-"*50
		_AssetAssignation = {}
		Tots = []
		j = 1
		for k, bid in self.Bids.iteritems():
			vals = []
			i = 1
			TotalLoan = 0
			for a in self.Loans:
				if j == 1:
					Tots.append(0)
				if a['MO'] == 'Total':
					vals.append(TotalLoan)
					Tots[i-1] = Tots[i-1] + TotalLoan
				elif ((self.SpecifiedCompetitive(k, True, Competitive) and bid['sperate'] != [])
						and ((bid['loannum'] != '' and int(bid['loannum']) == i)
							or (bid['loannum'] == '' and bid['mo'] == a['MO']))):
					l = bid['sperate'] * a['Load Amount']
					vals.append(l)
					Tots[i-1] = Tots[i-1] + l
					TotalLoan = TotalLoan + l
				else:
					vals.append(0)
				i = i+1
			if self.options.Verbose:
				print k,
				print vals
			_AssetAssignation[k] = vals
			j = j + 1
		_AssetAssignation['Total'] = Tots 
		if self.options.Verbose:
			print "Total ",
			print Tots
		return _AssetAssignation

	def WARate(self, asset):
		'''Take the asset and the column bidrate of bid and make a inner
		product of each column with this rate, after that divide by the total
		amount of the sum of each column of the asset, ie, make a ponderation
		of the rate by the asset by each column.''and make a inner product of
		each column with this rate, after that divide by the total amount of
		the sum of each column of the asset, ie, make a ponderation of the rate
		by the asset by each column.'''
		_WARate = []	
		TotRate = 0
		for i in range(len(self.Loans)-1):
			rate = 0
			for k, a in self.Bids.iteritems():
				if a['bidrate']:
					rate = rate + asset[k][i] * a['bidrate']
			if rate:
				TotRate = TotRate + rate
			if asset['Total'][i]:
				rate = rate / asset['Total'][i]
			else:
				rate = None
			_WARate.append(rate)
		TotRate = TotRate / asset['Total'][len(self.Loans)-1] if asset['Total'][len(self.Loans)-1] != 0 else 0
		_WARate.append(TotRate)
		return _WARate

	def WARateSNC(self, assetSC, assetSNC):
		_WARateSNC = []
		LoansRates = map (lambda x : x['Rate'], self.Loans[0:-1])
		SCummulative = map (lambda x,y: x+y, assetSC['Total'], assetSNC['Total'])
		_WARateSNC = LoansRates
		s = sum(map (lambda x,y: x*y, assetSNC['Total'][0:-1], _WARateSNC))
		s = s / assetSNC['Total'][-1] if assetSNC['Total'][-1] != 0 else 0
		_WARateSNC.append(s)
		return _WARateSNC

	def WARateS(self, assetSC, WARateSC, assetSNC, WARateSNC):
		g = lambda x, y, w, z: x == None or y == None or w == None or z == None
		c = map ( lambda asc, wsc, asnc, wsnc: ((1 if (asc + asnc != 0) else None)
				if g (asc, wsc, asnc, wsnc) else 0),
				assetSC['Total'][0:-1], WARateSC[0:-1],
				assetSNC['Total'][0:-1], WARateSNC[0:-1])
		d = map (lambda x, y: y if x else (0 if x == 0 else None), c, WARateSNC[0:-1])  
		try:
			_WARateS = map (lambda x, asc, wsc, asnc, wsnc:
					(asc*wsc + asnc*wsnc)/(asc + asnc) if x == 0 else (x if 
						x != None else 0), d, assetSC['Total'][0:-1], WARateSC[0:-1],
					assetSNC['Total'][0:-1], WARateSNC[0:-1])
		except:
			sys.exit("Error: Try with a non cero rate in the --priordayrateused " +
					"parameter") 	
		_WARateS.append((assetSC['Total'][-1]*WARateSC[-1] +
				assetSNC['Total'][-1]*WARateSNC[-1])/
				(assetSC['Total'][-1] + assetSNC['Total'][-1])
				if (assetSC['Total'][-1] + assetSNC['Total'][-1]) != 0 else 0)
		return _WARateS  

	def WARateTot(self, assetSC, assetSNC, assetGC, assetGNC, WARateGNC, WARateSGC):
		#G174:M174
		cummulativeSGC = map (lambda x, y, z: x+y+z, assetSC['Total'],
				assetSNC['Total'], assetGC['Total'])
		cummulativeT = map (lambda x, y: x+y, cummulativeSGC, assetGNC['Total'])
		s1 = map(lambda x, y: x*y, assetGNC['Total'], WARateGNC)
		s2 = map(lambda x, y: x*y, cummulativeSGC, WARateSGC)
		_w0 = map(lambda x, y, z: (x+y)/z if z != 0 else 0, s1, s2, cummulativeT)
		_w = map(lambda x, y, z: x if y == None else z, WARateGNC,
				WARateSGC, _w0)
		return _w

	def MarketPremium(self, assetSC, assetSNC, WARateS, PreWARateGC):
		# In 5.xlsx G145:L145
		_MarketPremiumPrim = []
		_MarketPremium = []
		_bidRates = map (lambda x: x['bidrate'] if x['bidrate'] != '' else 0,
				self.Bids.values())
		_moRates = map (lambda x: x['Rate'], self.Loans[0:-1])
		HighestDailyRate = max(_bidRates + _moRates)
		MarketRateDifferential = HighestDailyRate - WARateS[-1]
		Cummulative = map (lambda x, y: x+y, assetSC['Total'],
				assetSNC['Total'])
		Subscription = map (lambda x, y: x/y, Cummulative[0:-1],
				map ( lambda x:x['Load Amount'], self.Loans)[0:-1])
		_MarketPremiumPrim = map ( lambda x: (1 - x)*MarketRateDifferential,
				Subscription)
		_MarketPremium = map (lambda x, y, w, z: y if z > 0 and y >= w 
				else (y + x if x != None and y != None else 0) , _MarketPremiumPrim,
				PreWARateGC[0:-1], WARateS[0:-1], Cummulative[0:-1]) 
		return _MarketPremium

	def WARateGC(self, assetGC, MarketPremium):
		# In 5.xlsx G146:M146
		_WARateGC = map(lambda x: x, MarketPremium)
		s = sum(map(lambda x, y: x*y, assetGC['Total'][0:-1], MarketPremium))
		s = s/assetGC['Total'][-1] if assetGC['Total'][-1] != 0 else 0
		_WARateGC.append(s)
		return _WARateGC

	def WARateSGC(self, assetSC, assetSNC, assetGC, WARateS, MarketPremium):
		#G139:M139
		cummulativeS = map (lambda x, y: x+y, assetSC['Total'], assetSNC['Total'])
		cummulativeSGC = map (lambda x, y, z: x+y+z, assetSC['Total'],
				assetSNC['Total'], assetGC['Total'])
		s1 = map(lambda x, y: x*y, assetGC['Total'][0:-1], MarketPremium)
		s2 = map(lambda x, y: x*y if y != None else 0, cummulativeS[0:-1], WARateS[0:-1])
		__WARateSGC = map (lambda x, y, z: (x+y)/z if z != 0 else 0, s1, s2,
				cummulativeSGC[0:-1])
		_WARateSGC = map (lambda x, y, z: z if x != None else y, WARateS[0:-1], MarketPremium,
				__WARateSGC)
		_WARateSGC.append(sum(map (lambda x, y: x*y, cummulativeSGC[0:-1],
			_WARateSGC))/cummulativeSGC[-1] if cummulativeSGC[-1] != 0 else 0)
		return _WARateSGC 

	def WARateGNC(self, assetSC, assetSNC, assetGNC, WARateS, WARateGC, MarketPremium):
		#G171:M171 new G184:M184
		_WARateGNC = []
		_WARateGNC = map (lambda x, y: x if y == None else max(x, y) , MarketPremium, WARateS[0:-1])
		_r = max(WARateS[-1], WARateGC[-1])
		_WARateGNC.append(_r)
		return _WARateGNC

	def GetLoans(self):
		#TODO change by List Comprehensions
		L = []
		for i in self.Loans:
			L.append((i['Load Amount'], 'under'))
		return L

	def CalcRemaing (self, AssetAssigned, Loans):
		calc = []
		for i in zip(AssetAssigned['Total'], Loans):
			c = i[1][0] - i[0]
			#This line is added to reduce the error propagation
			if abs(c) < 1e-9: c = 0
			calc.append((c, None if c == 0 else "over" if c < 0 else "under"))
		if self.options.Verbose:
			print "Remained need"
			print calc
		return calc

	def GetMaxRateMOAccepted(self, asset, i):
		MO = self.Loans[i]['MO']
		l, m, j = [], 0, 0
		for lo in self.Loans:
			if i != j and MO == lo['MO']:
				l.append(j)
			j += 1

		if l != []:
			for k, a in asset.iteritems():
				for lo in l:
					if a[lo] > 0 and k != 'Total':
						m = max(self.Bids[k]['bidrate'] if self.Bids[k]['bidrate'] != '' else 0, m)
		return m

	def GetMaxRateAccepted(self, asset):
		m = 0
		for k, a in asset.iteritems():
			for lo in range(len(self.Loans)-1):
				if a[lo] > 0 and k != 'Total':
					m = max(self.Bids[k]['bidrate'] if self.Bids[k]['bidrate'] != '' else 0, m)
		return m

	def CalcLoansRatesSNC(self, assetSC):
		i = 0
		for v in self.Loans[:-1]:
			m = 0
			previousRate = v['Rate']
			for k, a in assetSC.iteritems():
				if a[i] > 0 and k != 'Total':
					m = max(self.Bids[k]['bidrate'] if self.Bids[k]['bidrate'] != '' else 0, m)
			if m == 0:
				m = self.GetMaxRateMOAccepted(assetSC, i)
			if m == 0:
				m = self.GetMaxRateAccepted(assetSC)
			#TODO see the General Competitive case
			#if m == 0:
			#	m = self.GetMaxRateGCAccepted()
			if m != 0:
				self.Loans[i]['Rate'] = m
			else:
				self.Loans[i]['Rate'] =  previousRate
			i += 1

	def AllocateGenericCompetitive(self, Rank):
		_AssetAlloAndAccept = {}
		TotalAggregate = 0
		TotalRate = 0
		for k, bid in self.Bids.iteritems():
			vals = {}
			if self.SpecifiedCompetitive(k, False, True):
				if (bid['bidrate'] > 0):
					#vals['aggregate'] = min(bid['aggregate'], bid['funds'])
					vals['aggregate'] = min(bid['aggregate'],
							self.Users[bid['userid']]['funds'])
					#TODO reduce funds to the user
					TotalAggregate = TotalAggregate + vals['aggregate']
					vals['rank'] = Rank[k]
					vals['bidrate'] = bid['bidrate']
					TotalRate = TotalRate + vals['aggregate'] * vals['bidrate']
				if self.options.Verbose:
					print k,
					print vals
				_AssetAlloAndAccept[k] = vals 
		if self.options.Verbose:
			print "Total " + str(TotalAggregate)
		Tot = {'aggregate': TotalAggregate, 'bidrate': TotalRate /
				TotalAggregate if TotalAggregate != 0 else 0}
		_AssetAlloAndAccept['Total'] = Tot
		return _AssetAlloAndAccept 

	def AdjustRankWithAllocateAndAccepted(self, Allocate, Rank, Rem):
		V = {}	
		rk = sorted(Rank)
		v = Allocate['Total']['aggregate'] - Rem[len(Rem)-1][0]
		for k in rk:
			if v > 0:
				v0 = min (Allocate[k]['aggregate'], v)
			else:
				v0 = 0
			v = v - v0
			V[k] = (v0, v) 
		return V

	def AdjustAllocateAndAccepted(self, Allocate, VRank, AmmountRequired):
		vallow = Allocate
		for k, v in vallow.iteritems():
			vallow[k]['allocated'] = 0.0
		Tot = 0
		if self.options.AllocAcceptException:
			AmtRequired = deepcopy(AmmountRequired)
			i = 1
			l = len(vallow)
			while AmtRequired > 0.0 and i <= l:
				for k, v in Allocate.iteritems():
					if k != 'Total' and v['rank'] == i:
						vallow[k]['allocated'] =  min (AmtRequired, v['aggregate'])
						Tot = Tot + vallow[k]['allocated']
						AmtRequired = AmtRequired - vallow[k]['allocated']
				i += 1
		else:
			for i in Allocate.iteritems():
				if i[0] != 'Total':
					vallow[i[0]]['v0'] = VRank[i[0]][0]
					vallow[i[0]]['allocated'] = i[1]['aggregate'] - VRank[i[0]][0]
					Tot = Tot + vallow[i[0]]['allocated']
		vallow['Total']['allocated'] = Tot
		return vallow 

	def GenericAssetAssignation(self, Rem, Allocate):
		if self.options.Verbose:
			print "-"*50
		_AssetAssignation = {}
		Tots = []
		j = 1
		PTot = len(Rem) - 1
		for k, bid in self.Bids.iteritems():
			vals = []
			i = 1
			TotalLoan = 0
			for a in self.Loans:
				if j == 1:
					Tots.append(0)
				if not Allocate.has_key(k):
					vals.append(0)
				elif a['MO'] == 'Total':
					vals.append(TotalLoan)
					Tots[i-1] = Tots[i-1] + TotalLoan
				else:
					l = Allocate[k]['allocated']* Rem[i-1][0] / Rem[PTot][0]
					vals.append(l)
					Tots[i-1] = Tots[i-1] + l
					TotalLoan = TotalLoan + l
				i = i+1
			if self.options.Verbose:
				print k,
				print vals
			_AssetAssignation[k] = vals
			j = j + 1
		_AssetAssignation['Total'] = Tots 
		if self.options.Verbose:
			print "Total ",
			print Tots
		return _AssetAssignation

	def CalcRateAwarded(self, assetGC, allocate, SNCompAssetRem, WARateGC,
			MarketPremium):
		_L = []
		i = 0
		for a in self.Loans:
			rate = 0
			for k, d in allocate.iteritems():
				if k != 'Total':
					rate = rate + assetGC[k][i] * allocate[k]['bidrate']
			_L.append(rate / assetGC['Total'][i] if assetGC['Total'][i] != 0
					else 0)
			i = i+1
		_LoanRates = map(lambda x, y: x - y, WARateGC, _L)
		_Rates = {}	
		_RatesTot = 0
		for k, d in allocate.iteritems():
			if k != 'Total':
				rate = 0
				for i in range(0, len(_LoanRates) - 1):
					rate = rate + _LoanRates[i] * assetGC[k][i] 
				_Rates[k] = {'rate': allocate[k]['bidrate'], 'rateawarded':
						allocate[k]['bidrate'] + (rate /
						assetGC[k][-1] if assetGC[k][-1] != 0 else 0)} 
				_RatesTot = _RatesTot + _Rates[k]['rateawarded'] * allocate[k]['allocated']
		_Rates['Total'] = {'rateawarded':_RatesTot /
				allocate['Total']['allocated'] if
				allocate['Total']['allocated'] != 0 else 0} 
		return _Rates

	def AllocateGenericNonCompetitive(self, GCompAssetRem):
		_AssetAlloAndAccept = {}
		TotalAggregate = 0
		for k, bid in self.Bids.iteritems():
			if self.SpecifiedCompetitive(k, False, False):
				#TotalAggregate = TotalAggregate + bid['funds'] 
				TotalAggregate = TotalAggregate + self.Users[bid['userid']]['funds'] 
				
		rate = GCompAssetRem[len(GCompAssetRem)-1][0]/TotalAggregate if TotalAggregate != 0 else 0
		TotalAggregate = 0
		for k, bid in self.Bids.iteritems():
			vals = {}
			if self.SpecifiedCompetitive(k, False, False):
				#vals['allocated'] = bid['funds'] * rate
				vals['allocated'] = self.Users[bid['userid']]['funds'] * rate
				TotalAggregate = TotalAggregate + vals['allocated']
				_AssetAlloAndAccept[k] = vals
				if self.options.Verbose:
					print k,
					print vals
		Tot = {'aggregate': TotalAggregate, 'bidrate': rate}
		_AssetAlloAndAccept['Total'] = Tot
		return _AssetAlloAndAccept
	
	def SummaryVals(self, j, k, vals, Tots, assetSC, assetSNC, assetGC,
			assetGNC, GNComptAssetRem):
		i = 1
		TotalLoan = 0
		for a in self.Loans:
			if j == 1:
				Tots.append(0)
			if a['MO'] == 'Total':
				vals.append(TotalLoan)
				Tots[i-1] = Tots[i-1] + TotalLoan
			else:
				l = assetSC[k][i-1] + assetSNC[k][i-1] + assetGC[k][i-1] + \
						assetGNC[k][i-1] if GNComptAssetRem[i-1][1] == None else 0
				vals.append(l)
				Tots[i-1] = Tots[i-1] + l
				TotalLoan = TotalLoan + l
			i = i+1

	def Summary(self, assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
			WARateTot, GNComptAssetRem):
		#TODO remove the variables that are don't used, 
		#but before print in the format with titles WARateTot and the others
		#TODO remove to the prints, and move to the Print Summary function
		if self.options.Verbose:
			print "-"*50
		if self.options.output:
			ofile = open(self.options.output, "wb")
			summwrt = csv.writer(ofile, delimiter=self.options.delimiter, quotechar='"')
		_AssetAssignation = {}
		vals = []
		Tots = []
		j = 1
		for k, bid in self.Bids.iteritems():
			vals = []
			self.SummaryVals(j, k, vals, Tots, assetSC, assetSNC,
					assetGC, assetGNC, GNComptAssetRem)
			_AssetAssignation[k] = vals
			j = j + 1
		_AssetAssignation['Total'] = Tots
		if self.options.Verbose or not self.options.output:
			print "Total ",
			print Tots
		if self.options.output:
			summwrt.writerow(["Total"] + Tots)
			ofile.close()
		return _AssetAssignation
	
	def SumRateAllocation(self, asset, assetSNC, ratesGC, WARateGNC):
		_all = {}
		for k, bid in self.Bids.iteritems():
			rate = 0
			# Add rate from Generic Competitive Awarded
			if self.SpecifiedCompetitive(bid = k, specified = True, competitive
				= True):
				rate = rate + bid['bidrate']  
			# Add the weighted rate for Specified Noncompetitive 
			_LoanRates = map(lambda x: x['Rate'] if x.has_key('Rate') else None,
					self.Loans)[0:-1]
			rate = rate + (sum(map(lambda x,y: x*y, _LoanRates,
				assetSNC[k][0:-1]))/assetSNC[k][-1] if assetSNC[k][-1] != 0 else 0)
			rate = rate if asset[k][-1] > 0 else 0
			if ratesGC.has_key(k):
				rate = rate + ratesGC[k]['rateawarded']
			rate = rate if asset[k][-1] > 0 else 0
			rate = rate + (WARateGNC[-1] if self.SpecifiedCompetitive(bid = k, specified = False, competitive =
					False) else 0)
			_all[k] = rate
		return _all

	def PrintSummary(self, asset, AllocRates):
		if self.options.Verbose:
			print "-"*50
			print "Asset Summary"
			print "-"*50
		if self.options.output:
			ofile = open(self.options.output, "wb")
			summwrt = csv.writer(ofile, delimiter=self.options.delimiter, quotechar='"')
		valsRate = 0
		for k, bid in self.Bids.iteritems():
			# Print in standart output if there are no output or there are
			# verbose option.
			if self.options.Verbose or not self.options.output:
				print k,
				print asset[k],
				print AllocRates[k]
			valsRate = valsRate + AllocRates[k] * asset[k][-1]
		valsRate = valsRate / asset['Total'][-1]
		if self.options.Verbose or not self.options.output:
			print "Total ",
			print asset['Total'],
			print valsRate

	def LoadAsConsole(self):
		self.LoadMortgageOperators()
		self.LoadLoans()
		self.LoadUsers()
		self.LoadBids()
		self.LoadExceptions()

	def Calc(self):
		# Calculate Specified and Competitive Assets
		if self.options.Verbose:
			print "Assets are assigned Specified/Competitive bids"
		assetSC = self.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.WARate(assetSC)
		SCompAssetRem = self.CalcRemaing (assetSC, self.GetLoans())

		# Calculate Specified and Noncompetitive Assets
		self.CalcLoansRatesSNC(assetSC)
		if self.options.Verbose:
			print "Assets are assigned Specified/Non Competitive bids"
		assetSNC = self.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.WARateSNC(assetSC, assetSNC)

		# Summary the Specified rates
		WARateS = self.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)

		# Calculate General and Competitive Assets
		if self.options.Verbose:
			print "General/Competitive bids are assigned to undersubscribed assets"
			print 50*"-"
		rank = self.RankRateGenericCompetitive()
		allocateGC = self.AllocateGenericCompetitive(Rank = rank)
		valrank = self.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC, 
				Rank = rank, Rem = SNCompAssetRem)
		self.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank,
				AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))

		#Generate Generic asset for Competitive
		assetGC = self.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
				allocateGC)
		GCompAssetRem = self.CalcRemaing (assetGC, SNCompAssetRem)
		MarketPremium = self.MarketPremium(assetSC, assetSNC, WARateS,
				self.WARate(assetGC))
		WARateGC = self.WARateGC(assetGC, MarketPremium)
		WARateSGC = self.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
				MarketPremium)
		ratesGC = self.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
				WARateGC, MarketPremium)

		# Calculate General and Noncompetitive Assets
		if self.options.Verbose:
			print "General/Noncompetitive bids are assigned to undersubscribed assets"
		allocateGNC = self.AllocateGenericNonCompetitive(GCompAssetRem)
		assetGNC = self.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
				allocateGNC)
		WARateGNC = self.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
				WARateGC, MarketPremium)
		#G177:M177
		GNComptAssetRem = self.CalcRemaing (assetGNC, GCompAssetRem)

		WARateTot = self.WARateTot(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateSGC)
		# Make the summary of the assets
		asset = self.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateTot, GNComptAssetRem)
		AllocRates = self.SumRateAllocation( asset, assetSNC, ratesGC, WARateGNC)
		self.PrintSummary(asset, AllocRates)

	def main(self, *args):
		self.LoadAsConsole()
		self.Calc()

if __name__ == '__main__':
	app = LiqEngine()
	sys.exit(app.main(*sys.argv))
