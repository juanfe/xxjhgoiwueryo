from django.db import models

#TODO see if it is possible to change all this to dojango-datable
class Loan(models.Model):
	Loanid = models.CharField(max_length = 40, verbose_name = "Loan Id")
	Funded = models.BooleanField(verbose_name = "Is Funded")
	#MortgageOriginator = models.CharField(max_length = 40,
	#		verbose_name = "Mortgage Originator")
	InvestorRate = models.DecimalField(max_digits = 13, decimal_places = 9,
			verbose_name = "Investor Rate", null = True)
	RateToMo = models.DecimalField(max_digits = 13, decimal_places = 9,
			verbose_name = "Rate to Mortgage Originator", null = True)
	#TODO pass to MoneyField
	FundedAmount = models.FloatField(verbose_name = "Founded Amount")

class Bid(models.Model):
	#TODO assign a foreignkey to Bids.models.Bid
	BidId = models.CharField(max_length = 40, verbose_name = "Bid Id")
	#Date = models.DateTimeField(auto_now = True,  verbose_name = "Date and Time")
	#Todo see if there a a way to split the date and time
	#time = models.DateTimeField(auto_now = True)
	#BidType = models.CharField(max_length = 40, verbose_name = "Bid Type")
	#Participation =  models.DecimalField(max_digits = 13, decimal_places = 9,
	#		verbose_name = "Participation", null = True)
	#AssetSubset = models.CharField(max_length = 40, verbose_name = "Asset Subset")
	#LoanId = models.CharField(max_length = 40, verbose_name = "Loan Id")
	#OrderType = models.CharField(max_length = 40, verbose_name = "Order Type")
	#BidRate = models.DecimalField(max_digits = 13, decimal_places = 9,
	#		verbose_name = "Bid Rate", null = True)
	#OrderTiming = models.CharField(max_length = 40, verbose_name = "Order Timing")
	#UserId = models.CharField(max_length = 40, verbose_name = "User's Mail")
	AcceptedRate = models.DecimalField(max_digits = 13, decimal_places = 9,
		verbose_name = "Accepted Rate", null = True)
	FundsTotal = models.FloatField(verbose_name = "Funds Total")

class BidsAllocation(models.Model):
	bid = models.ForeignKey(Bid)
	loan = models.ForeignKey(Loan) 
	AllocatedAmount = models.FloatField(verbose_name = "Allocated Amount")

class UserFunds(models.Model):
	User = models.CharField(max_length = 40, verbose_name = "User's Mail")
	#TODO pass to MoneyField
	Funds =  models.FloatField(verbose_name = "Funds Available")
