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
		self.app = LiqEngine()
		self.app.ParseArg()
		assert self.app.options.OperatorFilename == p 

	def test_LoadMortgageOperators(self, arg, p):
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		assert self.app.Mo ==  p

	def test_addLoans(self, arg, p, q, r):
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		flo = csv.reader(open(self.app.options.loansFilename, "rb"),
				delimiter=self.app.options.delimiter,quoting=csv.QUOTE_NONE)
		idlo = flo.next()
		idlo.append("Rate")
		assert idlo == p
		lo = flo.next()
		lo.append(str(float(self.app.options.PriorRate)/100))
		assert lo == q
		self.app.addLoans(idlo, lo)
		assert self.app.Loans == r

	def test_LoadLoans(self, arg, p):
		#In engine processing rules example.xlsx G4:M4
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		assert self.app.Loans == p

	def test_LoadBids(self, arg, p, q, r):
		#In engine processing rules example.xlsx bid input!G4:N4
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		assert len(self.app.Bids) == p
		assert self.app.Bids[q] == r

	def test_LoadExceptions(self, arg):
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assert self.app.Exceptions == []

	def test_SpecifiedAssetAssignation(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G8:M27
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		assert  assetSC == p

	def test_WARateSC(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G30:M30
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		assert WARateSC == p

	def test_CalcRemaing(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G32:M33
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		assert SCompAssetRem == p 

	def test_WARateSNC(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G59:M59
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		assert WARateSNC == p

	def test_WARateS(self, arg, p, q):
		#In engine processing rules example.xlsx "assets availale for bid"!G67:M67
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank =
				valrank, AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))
		WARateS = self.app.WARateS(assetSC, WARateSC, assetSNC, WARateSNC)
		assert WARateS == p
		assert allocateGC == q

	#TODO add lines to test WARateGC in this test, and test in the test5
	def test_CalcRateAwarded(self, arg, p):
		#In engine processing rules example.xlsx
		# For rate "assets availale for bid"!C106:C125
		# For rateawarded "assets availale for bid"!E106:E125
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank =
				valrank, AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))
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
		assert ratesGC == p

	def test_WARateTot(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G174:G174
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank =
				valrank, AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))
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
				WARateGC, MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				WARateGNC, WARateSGC)
		assert WARateTot == p

	def test_Summary(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!G182:M202
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank =
				valrank, AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))
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
				WARateGC, MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				WARateGNC, WARateSGC)
		sum = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateTot, GNComptAssetRem)
		assert sum == p

	def test_SumRateAllocation(self, arg, p):
		#In engine processing rules example.xlsx "assets availale for bid"!C182:C201
		sys.argv = arg
		self.app = LiqEngine()
		self.app.LoadMortgageOperators()
		self.app.LoadLoans()
		self.app.LoadUsers()
		self.app.LoadBids()
		self.app.LoadExceptions()
		assetSC = self.app.SpecifiedAssetAssignation(Competitive = True)
		WARateSC = self.app.WARate(assetSC)
		SCompAssetRem = self.app.CalcRemaing (assetSC, self.app.GetLoans())
		self.app.CalcLoansRatesSNC(assetSC)
		assetSNC = self.app.SpecifiedAssetAssignation(Competitive = False)
		SNCompAssetRem = self.app.CalcRemaing (assetSNC, SCompAssetRem)
		WARateSNC = self.app.WARateSNC(assetSC, assetSNC)
		rank = self.app.RankRateGenericCompetitive()
		allocateGC = self.app.AllocateGenericCompetitive(Rank = rank)
		valrank = self.app.AdjustRankWithAllocateAndAccepted(Allocate = allocateGC,
				Rank = rank, Rem = SNCompAssetRem)
		self.app.AdjustAllocateAndAccepted(Allocate = allocateGC, VRank =
				valrank, AmmountRequired = (SNCompAssetRem[-1][0] if
					SNCompAssetRem[-1][1] == 'under' else 0))
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
				WARateGC, MarketPremium)
		GNComptAssetRem = self.app.CalcRemaing (assetGNC, GCompAssetRem)	
		WARateTot = self.app.WARateTot(assetSC, assetSNC, assetGC, assetGNC,
				WARateGNC, WARateSGC)
		asset = self.app.Summary(assetSC, assetSNC, assetGC, assetGNC, WARateGNC,
				WARateTot, GNComptAssetRem)
		AllocRates = self.app.SumRateAllocation(asset, assetSNC, ratesGC, WARateGNC)
		assert AllocRates == p
