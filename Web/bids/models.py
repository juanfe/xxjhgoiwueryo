import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

class Bid(models.Model):
	TYPE_CHOICES = (
			('G', 'General'),
			('S', 'Specified'),
	)
	LOAN_CHOICES = (
			('M', 'Mortgage Originator'),
			('L', 'Loan'),
	)
	ORDER_CHOICES = (
			('A', 'Auto'),
			('D', 'Day Trade'),
	)
	#User = models.ForeignKey()
	Time = models.DateTimeField(auto_now = True)
	Type = models.CharField(max_length = 1, choices = TYPE_CHOICES)
	Aggregated = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency = moneyed.USD)
	F = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency = moneyed.USD)
	AggregatedDate = models.DateTimeField(auto_now = True)
	Percentage = models.DecimalField(max_digits = 15, decimal_places = 14)
	LoanType = models.CharField(max_length = 1, choices = LOAN_CHOICES)
	Competitive = models.BooleanField()
	CompetitiveRate = models.DecimalField(max_digits = 15, decimal_places = 14)
	OrderTiming = models.CharField(max_length = 1, choices = ORDER_CHOICES)
	#FundsAvailable = MoneyField(max_digits = 20, decimal_places = 9,
	#		default_currency = moneyed.USD)
	FundsAvailableDate = models.DateTimeField(auto_now = True)
