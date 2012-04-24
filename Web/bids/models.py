import moneyed
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
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
	STATUS_CHOICES = (
			('K', 'Accepted'),
			('A', 'Active'),
			('C', 'Cancelled'),
	)
	User = models.ForeignKey(User)
	CreatedAt = models.DateTimeField(auto_now = True)
	ExpiresAt = models.DateTimeField(auto_now = True)
	Type = models.CharField(max_length = 1, choices = TYPE_CHOICES)
	Aggregated = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency = moneyed.USD)
	AggregatedDate = models.DateTimeField(auto_now = True)
	Participation = models.DecimalField(max_digits = 13, decimal_places = 9)
	LoanType = models.CharField(max_length = 1, choices = LOAN_CHOICES)
	Competitive = models.BooleanField()
	CompetitiveBidRate = models.DecimalField(max_digits = 13, decimal_places = 9)
	OrderTiming = models.CharField(max_length = 1, choices = ORDER_CHOICES)
	FundsAvailable = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency = moneyed.USD)
	FundsAvailableDate = models.DateTimeField(auto_now = True)
	Status = models.CharField(max_length = 1, choices = STATUS_CHOICES)
