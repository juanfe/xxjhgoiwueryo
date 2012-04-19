import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

class MortgageOriginator(models.Model):
	Name = models.CharField(max_length=200)
	#Contact = models.ForeignKey()

	def __unicode__(self):
		return self.Name

class Loans(models.Model):
	MortgageOriginator = models.ForeignKey(MortgageOriginator)
	Amount = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency=moneyed.USD)
	AmountDate = models.DateTimeField(auto_now=True)
	Creation = models.DateTimeField(auto_now=True)
	Assignation = models.DateTimeField()
	Hiden = models.BooleanField()
