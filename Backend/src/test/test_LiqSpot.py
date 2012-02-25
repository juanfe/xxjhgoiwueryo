import sys
sys.path.append("../")
from LiqSpot import *
from scenario import Scenario

def pytest_generate_tests(metafunc):
	for funcargs in metafunc.cls.scenario[metafunc.function.__name__]:
		metafunc.addcall(funcargs=funcargs)

class TestApplication:
	scenario = Scenario 

	def test_init (self, arg, p):
		sys.argv = arg
		self.app = Application()
		self.app.ParseArg()
		assert self.app.options.OperatorFilename == p 

	def test_LoadMortgageOperators(self, arg, p):
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		assert self.app.Mo ==  p

	def test_addLoans(self, arg, p, q, r):
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		flo = csv.reader(open(self.app.options.loansFilename, "rb"),
				delimiter=self.app.options.delimiter,quoting=csv.QUOTE_NONE)
		idlo = flo.next()
		assert idlo == p
		lo = flo.next()
		assert lo == q
		self.app.addLoans(idlo, lo)
		assert self.app.Loans == r

	def test_LoadLoans(self, arg, p):
		#In engine processing rules example.xlsx G4:M4
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		assert self.app.Loans == p

	def test_LoadBids(self, arg, p, q, r):
		#In engine processing rules example.xlsx bid input!G4:N4
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		assert len(self.app.Bids) == p
		assert self.app.Bids[q] == r

	def test_LoadExceptions(self, arg):
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assert self.app.Exceptions == []

	def test_SpecifiedAssetAssignation(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G8:M27
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		assert  assetSC == p

	def test_WARateSC(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G30:M30
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		assert WARateSC == p

	def test_CalcRemaing(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G32:M33
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assert SCompAssetRem == p 

	def test_WARateSNC(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G59:M59
		sys.argv = arg
		self.app = Application()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		assert WARateSNC == p

#	def test_WARateS(self):
#		#In engine processing rules example.xlsx "assets availale for bid"!G67:M67
#		self.app.LoadMortgageOperators()
#		self.app.LoadLoans()
#		self.app.LoadBids()
#		self.app.LoadExceptions()
#		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
#		WARateSC = self.app.WARate(assetSC)
#		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
#		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
#		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
#		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
#		rank = self.app.RankRateGenericCompetitive()
#		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
#		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
#				Rank = rank, Rem = SNCompAssetRem)
#		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
#		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
#		assert WARateS == [0.021666666666666667, 0.0225, 0.03, 0.0475, 0.02375,
#				None, 0.03150890885353453]
#
#	def test_CalcRateAwarded(self):
#		#In engine processing rules example.xlsx
#		# For rate "assets availale for bid"!C106:C125
#		# For rateawarded "assets availale for bid"!E106:E125
#		self.app.LoadMortgageOperators()
#		self.app.LoadLoans()
#		self.app.LoadBids()
#		self.app.LoadExceptions()
#		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
#		WARateSC = self.app.WARate(assetSC)
#		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
#		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
#		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
#		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
#		rank = self.app.RankRateGenericCompetitive()
#		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
#		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
#				Rank = rank, Rem = SNCompAssetRem)
#		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
#		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
#		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
#				allocateGC)
#		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
#		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
#				WARateS, self.app.WARate(assetGC))
#		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
#		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
#				MarketPremium)
#		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
#				WARateGC, MarketPremium)
#		assert ratesGC == {'1104139': {'rateawarded': 0.038617011249892495, 'rate': 0.0225},
#			'1104138': {'rateawarded': 0.037367011249892494, 'rate': 0.02125},
#			'1104141': {'rateawarded': 0.0411170112498925, 'rate': 0.025},
#			'1104154': {'rateawarded': 0.046117011249892495, 'rate': 0.03},
#			'Total': {'rateawarded': 0.040308187720480726}}
#
#	def test_WARateTot(self):
#		#In engine processing rules example.xlsx "assets availale for bid"!G174:G174
#		self.app.LoadMortgageOperators()
#		self.app.LoadLoans()
#		self.app.LoadBids()
#		self.app.LoadExceptions()
#		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
#		WARateSC = self.app.WARate(assetSC)
#		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
#		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
#		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
#		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
#		rank = self.app.RankRateGenericCompetitive()
#		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
#		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
#				Rank = rank, Rem = SNCompAssetRem)
#		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
#		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
#		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
#				allocateGC)
#		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
#		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
#				WARateS, self.app.WARate(assetGC))
#		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
#		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
#				MarketPremium)
#		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
#				WARateGC, MarketPremium)
#		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
#		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
#				                        allocateGNC)
#		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
#				                        self.app.WARate(assetGC), MarketPremium)
#		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
#		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
#				WARateGNC, WARateSGC)
#		assert WARateTot == [0.021919117647058825, 0.023514705882352945,
#				0.043587239510208486, 0.04500070978502713,
#				0.023926470588235292, 0.05268226761705371,
#				0.03639232973089888]
#
#	def test_Summary(self):
#		#In engine processing rules example.xlsx "assets availale for bid"!G182:M202
#		self.app.LoadMortgageOperators()
#		self.app.LoadLoans()
#		self.app.LoadBids()
#		self.app.LoadExceptions()
#		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
#		WARateSC = self.app.WARate(assetSC)
#		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
#		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
#		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
#		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
#		rank = self.app.RankRateGenericCompetitive()
#		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
#		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
#				Rank = rank, Rem = SNCompAssetRem)
#		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
#		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
#		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
#				allocateGC)
#		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
#		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
#				WARateS, self.app.WARate(assetGC))
#		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
#		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
#				MarketPremium)
#		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
#				WARateGC, MarketPremium)
#		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
#		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
#				                        allocateGNC)
#		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
#				                        self.app.WARate(assetGC), MarketPremium)
#		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
#		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
#				WARateGNC, WARateSGC)
#		sum = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
#				WARateTot, GNComptAssetRem)
#		assert sum == {'1104139': [5543.299916135251, 39203.726641962916,
#				66768.3061512063, 18275.628055141333, 35857.31096429852,
#				84351.72827125568, 250000.0],
#			'1104138': [6651.959899362301, 47044.471970355495, 80121.96738144755,
#				21930.7536661696, 43028.773157158226, 101222.07392550682, 300000.0],
#			'1104161': [0, 0, 0, 105080.0, 0, 0, 105080.0],
#			'1104152': [0, 0, 95975.0, 105080.0, 0, 0, 201055.0],
#			'1104131': [3913.036502380041, 27674.05980196056, 47132.00135739895, 12900.83538066028,
#				25311.812242393706, 59544.20593471866, 176475.9512195122],
#			'1104133': [0, 0, 0, 105080.0, 0, 0, 105080.0],
#			'1104134': [1226.9136190572872, 8677.067245598002, 14778.010459050674,
#				4044.994371026426, 7936.395979011404, 18669.797011303926,
#				55333.17868504772],
#			'1104136': [0, 0, 0, 105080.0, 0, 0, 105080.0],
#			'1104140': [0, 0, 0, 0, 103085.0, 0, 103085.0],
#			'1104141': [6319.361904394186, 44692.248371837726, 76115.86901237519,
#				20834.21598286112, 40877.33449930031, 96160.97022923148, 285000.0],
#			'1104151': [63745.0, 0, 0, 0, 0, 0, 63745.0],
#			'1104143': [63745.0, 75137.0, 0, 0, 0, 0, 138882.0],
#			'1104157': [4115.886220730846, 29108.668253232765, 49575.299086628664,
#				13569.60778333665, 26623.96304425692, 62630.94570725424,
#				185624.3700954401],
#			'1104145': [31872.5, 0, 0, 0, 0, 0, 31872.5],
#			'1104155': [0, 0, 0, 0, 103085.0, 0, 103085.0],
#			'1104154': [4102.0419379400855, 29010.757715052558, 49408.546551892665,
#				13523.964760804587, 26534.410113580907, 62420.2789207292, 185000.0],
#			'1104149': [0, 0, 0, 0, 103085.0, 0, 103085.0],
#			'1104159': [63745.0, 0, 0, 0, 0, 0, 63745.0],
#			'1104158': [63745.0, 0, 0, 0, 0, 0, 63745.0],
#			'1104156': [0, 75137.0, 0, 0, 0, 0, 75137.0],
#			'Total': [318725.0, 375685.00000000006, 479874.99999999994, 525400.0,
#				515425.0, 485000.0, 2700110.0]}
#
#	def test_SumRateAllocation(self):
#		#In engine processing rules example.xlsx "assets availale for bid"!C182:C201
#		self.app.LoadMortgageOperators()
#		self.app.LoadLoans()
#		self.app.LoadBids()
#		self.app.LoadExceptions()
#		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
#		WARateSC = self.app.WARate(assetSC)
#		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
#		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
#		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
#		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
#		rank = self.app.RankRateGenericCompetitive()
#		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
#		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
#				Rank = rank, Rem = SNCompAssetRem)
#		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank = valrank)
#		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
#		assetGC = self.app.GenericAssetAssignation(Rem = SNCompAssetRem, Allocate =
#				allocateGC)
#		GCompAssetRem = self.app.CalcRemaing (assetGC, SNCompAssetRem)
#		MarketPremium = self.app.MarketPremium(assetSC, assetSNC,
#				WARateS, self.app.WARate(assetGC))
#		WARateGC = self.app.WARateGC(assetGC, MarketPremium)
#		WARateSGC = self.app.WARateSGC(assetSC, assetSNC, assetGC, WARateS,
#				MarketPremium)
#		ratesGC = self.app.CalcRateAwarded(assetGC, allocateGC, SNCompAssetRem,
#				WARateGC, MarketPremium)
#		allocateGNC = self.app.AllocateGenericNonCompetitive(GCompAssetRem)
#		assetGNC = self.app.GenericAssetAssignation(Rem = GCompAssetRem, Allocate =
#				                        allocateGNC)
#		WARateGNC = self.app.WARateGNC(assetSC, assetSNC, assetGNC, WARateS,
#				                        self.app.WARate(assetGC), MarketPremium)
#		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
#		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
#				WARateGNC, WARateSGC)
#		asset = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
#				WARateTot, GNComptAssetRem)
#		AllocRates = self.app.SumRateAllocation(asset, assetSNC, ratesGC, WARateGNC)
#		assert AllocRates == {'1104139': 0.038617011249892495,
#				'1104138': 0.037367011249892494,
#				'1104161': 0.060000000000000005,
#				'1104152': 0.03, '1104131': 0.04159556720964421,
#				'1104133': 0.04, '1104134': 0.04159556720964421,
#				'1104136': 0.06, '1104140': 0.025,
#				'1104141': 0.0411170112498925, '1104151': 0.0225,
#				'1104143': 0.022500000000000003,
#				'1104157': 0.04159556720964421, '1104145': 0.015,
#				'1104155': 0.02125, '1104154': 0.046117011249892495,
#				'1104149': 0.025, '1104159': 0.0225, '1104158': 0.0225,
#				'1104156': 0.0225}

