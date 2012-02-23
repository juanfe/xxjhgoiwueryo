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
				'True', '-d', ',', '-M', '../mo.csv', '-o', 'test.csv'] #, '-v']
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
		assert lo == ['ABC Mortgage', '318725', '0.035']
		self.app.addLoans(idlo, lo)
		assert self.app.Loans == [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.035}]

	def test_LoadLoans(self):
		#In engine processing rules example.xlsx G4:M4
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		assert self.app.Loans == [{'MO': 'ABC Mortgage', 'Load Amount': 318725.0, 'Rate': 0.035},
			{'MO': 'ABC Mortgage', 'Load Amount': 375685.0, 'Rate': 0.035},
			{'MO': 'Prime Lending', 'Load Amount': 479875.0, 'Rate': 0.035},
			{'MO': 'Prime Lending', 'Load Amount': 525400.0, 'Rate': 0.035},
			{'MO': 'Best Loans Inc', 'Load Amount': 515425.0, 'Rate': 0.035},
			{'MO': 'Integrity Lending', 'Load Amount': 485000.0, 'Rate': 0.035},
			{'MO': 'Total', 'Load Amount': 2700110.0}]

	def test_LoadBids(self):
		#In engine processing rules example.xlsx bid input!G4:N4
		import datetime
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		assert len(self.app.Bids) == 20
		assert self.app.Bids['1104154'] == {'loannum': '2',
				'dateorder': datetime.datetime(2012, 1, 5, 9, 16), 'funds': 185000.0,
				'mo': '', 'time': datetime.datetime(1900, 1, 1, 15, 0),
				'bidrate': 0.03, 'competitive': True, 'ordertiming': 'Auto',
				'lorm': 'Loan', 'specified': True, 'aggregate': '', 'sperate': 0.2,
				'genrate': ''}

	def test_LoadExceptions(self):
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assert self.app.Exceptions == []

	def test_SpecifiedAssetAssignation(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G8:M27
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		assert  assetSC == {'1104139': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104138': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104161': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104152': [0, 0, 95975.0, 105080.0, 0, 0, 201055.0],
				'1104131': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104134': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
				'1104140': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104141': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104151': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104143': [63745.0, 75137.0, 0, 0, 0, 0, 138882.0],
				'1104157': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
				'1104155': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104154': [0, 75137.0, 0, 0, 0, 0, 75137.0],
				'1104149': [0, 0, 0, 0, 103085.0, 0, 103085.0],
				'1104159': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104158': [63745.0, 0, 0, 0, 0, 0, 63745.0],
				'1104156': [0, 75137.0, 0, 0, 0, 0, 75137.0],
				'Total': [414342.5, 225411.0, 95975.0, 525400.0, 618510.0, 0, 1879638.5]}

	def test_WARateSC(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G30:M30
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		assert WARateSC == [0.028269230769230772, 0.030000000000000002, 0.03,
				0.04025, 0.025625, None, 0.031043944088185043]

	def test_CalcRemaing(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G32:M33
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assert SCompAssetRem == [(-95617.5, 'over'), (150274.0, 'under'),
				(383900.0, 'under'), (0, None), (-103085.0, 'over'),
				(485000.0, 'under'), (820471.5, 'under')]

	def test_WARateSNC(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G59:M59
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
		assert WARateSNC == [0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0]

	def test_WARateS(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G67:M67
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
		assert WARateS == [0.028269230769230772, 0.030000000000000002, 0.03,
				0.04025, 0.025625, None, 0.031043944088185043]

	def test_CalcRateAwarded(self):
		#In engine processing rules example.xlsx
		# For rate "assets availale for bid"!C119:C138
		# For rateawarded "assets availale for bid"!E119:E138
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
		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
				allocateGC)
		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
				WARateS, self.app.WARate(assetGC))
		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
				MarketPremium)
		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
				WARateGC, MarketPremium)
		assert ratesGC == {'Total': {'rateawarded': 0}}

	def test_WARateTot(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G187:M187
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
		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
				allocateGC)
		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
				WARateS, self.app.WARate(assetGC))
		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
				MarketPremium)
		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
				WARateGC, MarketPremium)
		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
				                        allocateGNC)
		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
				                        self.app.WARate(assetGC), MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				WARateGNC, WARateSGC)
		assert WARateTot == [0.028269230769230772, 0.030000000000000002, 0.03,
				0.04025, 0.025625, 0, 0.031043944088185043]

	def test_Summary(self):
		#In engine processing rules example.xlsx "assets availale for bid"!G195:M215
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
		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
				allocateGC)
		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
				WARateS, self.app.WARate(assetGC))
		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
				MarketPremium)
		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
				WARateGC, MarketPremium)
		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
				                        allocateGNC)
		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
				                        self.app.WARate(assetGC), MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				WARateGNC, WARateSGC)
		sum = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateTot, GNComptAssetRem)
		assert sum == {'1104139': [0, 0, 0, 0, 0, 0, 0],
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
				'Total': [0, 0, 0, 525400.0, 0, 0, 525400.0]}

	def test_SumRateAllocation(self):
		#In engine processing rules example.xlsx "assets availale for bid"!C195:C214
		#Note: The values in the column C many are 0 by the adding of the
		#conditional D195>0, I will use the old formula by the moment
		#TODO change to include D195>0 in the previous formula, and see what
		#happen
		#In engine processing rules example.xlsx "assets availale for bid"!E195:E214
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
		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
				allocateGC)
		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
				WARateS, self.app.WARate(assetGC))
		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
				MarketPremium)
		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
				WARateGC, MarketPremium)
		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
				                        allocateGNC)
		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
				                        self.app.WARate(assetGC), MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				                WARateGNC, WARateSGC)
		asset = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC,
								WARateGNC, WARateTot, GNComptAssetRem)
		AllocRates = self.app.SumRateAllocation( asset, assetSNC, ratesGC, WARateGNC)
		assert AllocRates == {'1104139': 0, '1104138': 0.02125,
				'1104161': 0.0375, '1104152': 0.03, '1104131': 0.03375,
				'1104133': 0.04, '1104134': 0.03, '1104136': 0.06,
				'1104140': 0.025, '1104141': 0.025, '1104151': 0.035,
				'1104143': 0.03125, '1104157': 0.025, '1104145': 0.015,
				'1104155': 0.02125, '1104154': 0.03, '1104149': 0.03625,
				'1104159': 0.035, '1104158': 0.0225, '1104156': 0.02875}
