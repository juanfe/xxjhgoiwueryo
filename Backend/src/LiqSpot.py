#!/usr/bin/python

import csv, sys
from optparse import OptionParser
from datetime import datetime

class Application:
	def __init__(self):
		self.Mo = []
		self.Loans = []
		self.TotalLoans = 0
		self.Bids = {}
		self.Exceptions = []
		parser = self.ParseArg()
		(self.options, args) = parser.parse_args()
		return

	def ParseArg(self):
		parser = OptionParser()
	
		parser.add_option("-b", "--bids", dest="bidsFileName",
				help="Read the bids information.", metavar="BIDSFILE")
		parser.add_option("-l", "--loans", dest="loansFilename",
				help="Read the loan or mortgages information", metavar="LOANFILE")
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
				default="mo.csv",
				help = "Specify the Mortgage Operators, default mo.csv")
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
						% self.options.OperatorFilename)
		d['Load Amount'] = float(d['Load Amount'].strip(' '))
		d['Rate'] = float(d['Rate'].strip(' '))
		self.TotalLoans = self.TotalLoans + d['Load Amount']
		self.Loans.append(d)
	
	def LoadMortgageOperators(self):
		fmo = csv.reader(open(self.options.OperatorFilename, "rb"),
			delimiter=self.options.delimiter, quoting=csv.QUOTE_NONE)
		
		try:
			for op in fmo:
				if (op[0] != "Name"):

					self.Mo.append(op[0])
		except csv.Error, e:
			sys.exit('File %s, line %d: %s' % (self.options.OperatorFilename, fmo.line_num, e)) 
	
	def LoadLoans(self):
		try:
			flo = csv.reader(open(self.options.loansFilename, "rb"),
				delimiter=self.options.delimiter,quoting=csv.QUOTE_NONE)
		except:
			sys.exit('There are no parameter -l for the loan file name.')
		
		try:
			idlo = flo.next()
			for lo in flo:
				self.addLoans(idlo, lo)
			self.Loans.append({'MO': 'Total', 'Load Amount': self.TotalLoans})
		except csv.Error, e:
			sys.exit('File %s, line %d: %s' % (self.options.loansFilename, flo.line_num, e))

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
				"order timing":"ordertiming",
				"funds available":"funds",
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
				"ordertiming":"ordertiming",
				"funds":"funds",
				"dateorder":"dateorder"}

		for d in idbid:
			try:
				p = idbid.index(d)
				idbid[p] = dbid[d.lower()]	
			except:
				sys.exit('The column %s does not match witch the format' % (d) )

	def PriceToFloat(self, val):
		return val if val == '' else float(val.strip('$ ').replace(',',''))

	def RateToFloat(self, val):
		return val if val == '' else float(val.strip('% '))/100

	def cleanBidData(self, dbid):
		price = ['aggregate', 'funds']	
		for p in price:
			dbid[p] = self.PriceToFloat(dbid[p])
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

		#TODO add the today or the file date to the date
		dbid['time'] = datetime.strptime(dbid['time'], '%I:%M:%S %p')
		if dbid['dateorder'] != '':
			dbid['dateorder'] = datetime.strptime(dbid['dateorder'], '%m/%d/%y %I:%M %p')

	def addBids(self, idbid, b):
		dbid = dict(zip(idbid, b))
		id = dbid["id"]
		del(dbid["id"])
		self.cleanBidData(dbid)
		self.Bids[id] = dbid

	def LoadBids(self):
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
		R = sorted(R, key = lambda l: (l['bidrate'], l['time']), reverse=True)
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
		_WARateS = map (lambda x, asc, wsc, asnc, wsnc:
				(asc*wsc + asnc*wsnc)/(asc + asnc) if x == 0 else x,
				d, assetSC['Total'][0:-1], WARateSC[0:-1],
				assetSNC['Total'][0:-1], WARateSNC[0:-1])
		_WARateS.append((assetSC['Total'][-1]*WARateSC[-1] +
				assetSNC['Total'][-1]*WARateSNC[-1])/
				(assetSC['Total'][-1] + assetSNC['Total'][-1]))
		return _WARateS  

	def WARateTot(self, assetSC, assetSNC, assetGC, assetGNC, WARateGNC, WARateSGC):
		cummulativeSGC = map (lambda x, y, z: x+y+z, assetSC['Total'],
				assetSNC['Total'], assetGC['Total'])
		cummulativeT = map (lambda x, y: x+y, cummulativeSGC, assetGNC['Total'])
		s1 = map(lambda x, y: x*y, assetGNC['Total'], WARateGNC)
		s2 = map(lambda x, y: x*y, cummulativeSGC, WARateSGC)
		_w0 = map(lambda x, y, z: (x+y)/z if z != 0 else 0, s1, s2, cummulativeT)
		_w = map(lambda x, y, z: x if y == None else z, WARateGNC,
				WARateSGC, _w0)
		return None

	def MarketPremium(self, assetSC, assetSNC, WARateS, WARateGC):
		_MarketPremiumPrim = []
		_MarketPremium = []
		HighestDailyRate = max(map (lambda x: x['bidrate'] if x['bidrate'] !=
				'' else 0, 	self.Bids.values()))
		MarketRateDifferential = HighestDailyRate - WARateS[-1]
		Cummulative = map (lambda x, y: x+y, assetSC['Total'],
				assetSNC['Total'])
		Subscription = map (lambda x, y: x/y, Cummulative[0:-1],
				map ( lambda x:x['Load Amount'], self.Loans)[0:-1])
		_MarketPremiumPrim = map ( lambda x: (1 - x)*MarketRateDifferential,
				Subscription)
		_MarketPremium = map (lambda x, y, w, z: y if z > 0 and y >= w 
				else (y + x if x != None and y != None else 0) , _MarketPremiumPrim,
				WARateGC[0:-1], WARateS[0:-1], Cummulative[0:-1]) 
		return _MarketPremium

	def WARateGC(self, assetGC, MarketPremium):
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
			_WARateSGC))/cummulativeSGC[-1])
		return _WARateSGC 

	def WARateGNC(self, assetSC, assetSNC, assetGNC, WARateS, WARateGC,
			MarketPremium):
		_WARateGNC = []
		#_MarketPremium = self.MarketPremium(assetSC, assetSNC, WARateS, WARateGC)
		_WARateGNC = map (lambda x, y: x if y == None else max(x, y) , MarketPremium, WARateS[0:-1])
		_r = sum(map ( lambda x, y: x * y, _WARateGNC,
			assetGNC['Total'][0:-1]))
		_r = _r/assetGNC['Total'][-1] if assetGNC['Total'][-1] != 0 else 0
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
			if c < 1e-11: c = 0
			calc.append((c, None if c == 0 else "over" if c < 0 else "under"))
		if self.options.Verbose:
			print "Remained need"
			print calc
		return calc

	def AllocateGenericCompetitive(self, Rank):
		_AssetAlloAndAccept = {}
		TotalAggregate = 0
		TotalRate = 0
		for k, bid in self.Bids.iteritems():
			vals = {}
			if self.SpecifiedCompetitive(k, False, True):
				if (bid['bidrate'] > 0):
					vals['aggregate'] = min(bid['aggregate'], bid['funds'])
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

	def AdjustAllocateAndAccepted(self, Allocate, VRank):
		vallow = Allocate
		Tot = 0
		for i in Allocate.iteritems():
			#print i[0]['Total'] # != 'Total':
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
						allocate[k]['bidrate'] + rate /
						assetGC[k][len(_LoanRates)-1]} 
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
				TotalAggregate = TotalAggregate + bid['funds'] 
				
		rate = GCompAssetRem[len(GCompAssetRem)-1][0]/TotalAggregate if TotalAggregate != 0 else 0
		TotalAggregate = 0
		for k, bid in self.Bids.iteritems():
			vals = {}
			if self.SpecifiedCompetitive(k, False, False):
				vals['allocated'] = bid['funds'] * rate
				TotalAggregate = TotalAggregate + vals['allocated']
				_AssetAlloAndAccept[k] = vals
				if self.options.Verbose:
					print k,
					print vals
		Tot = {'aggregate': TotalAggregate, 'bidrate': rate}
		_AssetAlloAndAccept['Total'] = Tot
		return _AssetAlloAndAccept

	def SumRateAllocation(self, assetSC, assetSNC, assetGC, assetGNC, ratesGC,
			WARateGNC):
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
			if ratesGC.has_key(k):
				rate = rate + ratesGC[k]['rateawarded']
			rate = rate + (WARateGNC[-1] if self.SpecifiedCompetitive(bid = k, specified = False, competitive =
					False) else 0)
			_all[k] = rate
		return _all
	
	def SummaryVals(self, j, k, vals, Tots, assetSC, assetSNC, assetGC,
			assetGNC):
		i = 1
		TotalLoan = 0
		for a in self.Loans:
			if j == 1:
				Tots.append(0)
			if a['MO'] == 'Total':
				vals.append(TotalLoan)
				Tots[i-1] = Tots[i-1] + TotalLoan
			else:
				l = assetSC[k][i-1] + assetSNC[k][i-1] + assetGC[k][i-1] + assetGNC[k][i-1] 
				vals.append(l)
				Tots[i-1] = Tots[i-1] + l
				TotalLoan = TotalLoan + l
			i = i+1

	def Summary(self, assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
			WARateTot, AllocRates):
		#TODO remove the variables that are don't used, 
		#but before print in the format with titles WARateTot and the others
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
			self.SummaryVals(j, k, vals, Tots, assetSC, assetSNC,
					assetGC, assetGNC)
			# Print in standart output if there are no output or there are
			# verbose option.
			if self.options.Verbose or not self.options.output:
				print k,
				print AllocRates[k],
				print vals
			if self.options.output:
				summwrt.writerow([k, AllocRates[k]] + vals)
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
	
	def main(self, *args):
		self.LoadMortgageOperators()
		self.LoadLoans()
		self.LoadBids()
		self.LoadExceptions()

		# Calculate Specified and Competitive Assets
		assetSC = self.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.WARate(assetSC)
		SCompAssetRem = self.CalcRemaing (assetSC, self.GetLoans())

		# Calculate Specified and Noncompetitive Assets
		assetSNC = self.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.WARateSNC(assetSC, assetSNC)

		# Calculate General and Competitive Assets
		rank = self.RankRateGenericCompetitive()
		allocateGC = self.AllocateGenericCompetitive(Rank = rank)
		valrank = self.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC, 
				Rank = rank, Rem = SNCompAssetRem)
		self.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
		WARateS = self.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)

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
		allocateGNC = self.AllocateGenericNonCompetitive(GCompAssetRem)
		assetGNC = self.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
				allocateGNC)
		WARateGNC = self.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
				self.WARate(assetGC), MarketPremium)
		GNComptAssetRem = self.CalcRemaing (assetGNC, GCompAssetRem)
		AllocRates = self.SumRateAllocation(assetSC, assetSNC, assetGC, assetGNC, ratesGC,
				WARateGNC)

		WARateTot = self.WARateTot(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateSGC)
		# Make the summary of the assets
		self.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC, WARateTot, AllocRates)

if __name__ == '__main__':
	app = Application()
	sys.exit(app.main(*sys.argv))
