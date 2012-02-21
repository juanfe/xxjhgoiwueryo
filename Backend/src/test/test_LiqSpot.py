import sys
sys.path.append("../")
from LiqSpot import *
#import py.test

#def setup_module(module):
#	sys.argv = ['-b', '../sample/bids1.csv', '-l', '../sample/loans1.csv',
#			'True', '-d', '";"' '-o', 'test.csv', '-v']
#	module.TestApplication.

class TestApplication:
	def setup_method (self, method):
		sys.argv = ['-b', '../../sample/bids1.csv', '-l', '../../sample/loans1.csv',
				'True', '-d', ';', '-M', '../mo.csv', '-o', 'test.csv', '-v']
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

