import sys
sys.path.append("../")
from LiqSpot import *

#def setup_module(module):
#	sys.argv = ['-b', '../sample/bids1.csv', '-l', '../sample/loans1.csv',
#			'True', '-d', '";"' '-o', 'test.csv', '-v']
#	module.TestApplication.

class TestApplication:
	def setup_method (self, method):
		sys.argv = ['LiqSpot.py', '-b', '../../sample/bids1.csv', '-l', '../../sample/loans1.csv',
				'True', '-d', ';', '-M', '../mo.csv', '-o', 'test.csv'] #, '-v']
		self.app = Application()

	def test_init (self):
		self.app.ParseArg()
		assert self.app.options.OperatorFilename == '../mo.csv'

	def test_LoadMortgageOperators(self):
		self.app.LoadMortgageOperators()
		assert self.app.Mo == ['ABC Mortgage', 'Prime Lending', 'Best Loans Inc', 'Integrity Lending']

	def test_addLoans(self):
		self.app.LoadMortgageOperators()
		flo = csv.reader(open(self.app.options.loansFilename, "rb"),
				delimiter=self.app.options.delimiter,quoting=csv.QUOTE_NONE)
		idlo = flo.next()
		assert idlo == ['MO', 'Load Amount', 'Rate']
		lo = flo.next()
		assert lo == ['ABC Mortgage', ' 318725', ' 0.0225']
		self.app.addLoans(idlo, lo)
		assert self.app.Loans == [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.0225}]

	def test_LoadLoans(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		assert self.app.Loans == [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.0225},
			{'MO': 'ABC Mortgage', 'Load Amount': 375685.0, 'Rate': 0.0225},
			{'MO': 'Prime Lending', 'Load Amount': 479875.0, 'Rate': 0.03},
			{'MO': 'Prime Lending', 'Load Amount': 525400.0, 'Rate': 0.06},
			{'MO': 'Best Loans Inc', 'Load Amount': 515425.0, 'Rate': 0.025},
			{'MO': 'Integrity Lending', 'Load Amount': 485000.0, 'Rate': 0.06},
			{'MO': 'Total', 'Load Amount': 2700110.0}]

	def test_LoadBids(self):
		import datetime
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		assert len(self.app.Bids) == 20
		assert self.app.Bids['1104154'] == {'loannum': '',
				'dateorder': datetime.datetime(2012, 1, 5, 9, 16), 'funds': 185000.0,
				'mo': '', 'time': datetime.datetime(1900, 1, 1, 15, 0),
				'bidrate': 0.03, 'competitive': True, 'ordertiming': 'Auto', 'lorm': '',
				'specified': False, 'aggregate': 20000000.0, 'sperate': '',
				'genrate': 0.2}

	def test_LoadExceptions(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assert self.app.Exceptions == []

	def test_SpecifiedAssetAssignation(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		assert  assetSC == {'1104139': [0, 0, 0, 0, 0, 0, 0],
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
				'Total': [95617.5, 0, 95975.0, 315240.0, 206170.0, 0, 713002.5]}

	def test_WARate(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		assert WARateSC == [0.02, None, 0.03, 0.043333333333333335,
				0.023125, None, 0.03256605867440858]

	def test_CalcRemaing(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assert SCompAssetRem == [(223107.5, 'under'), (375685.0, 'under'),
				(383900.0, 'under'), (210160.0, 'under'), (309255.0, 'under'),
				(485000.0, 'under'), (1987107.5, 'under')]

	def test_WARateSNC(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		#SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		assert WARateSNC == [0.0225, 0.0225, 0.03, 0.06, 0.025, 0.06,
				0.03013764067429058]

	def test_WARateS(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
		assert WARateS == [0.021666666666666667, 0.0225, 0.03, 0.0475, 0.02375,
				None, 0.03150890885353453]

