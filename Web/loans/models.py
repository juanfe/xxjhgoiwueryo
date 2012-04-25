import moneyed
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.db import models

class MortgageOriginator(models.Model):
	Name = models.CharField(max_length=200)
	#TODO add user as foreignkey to contact
	#Contact = models.ForeignKey(User)

	def __unicode__(self):
		return self.Name

	#def create_MortgageOriginator(user)
	#	Name = user
	#	Contact = User.objects.get(username = user)

class Loan(models.Model):
	MortgageOriginator = models.ForeignKey(MortgageOriginator)
	Amount = MoneyField(max_digits = 20, decimal_places = 9,
			default_currency=moneyed.USD)
	AmountDate = models.DateTimeField(auto_now=True)
	Creation = models.DateTimeField(auto_now=True)
	Assignation = models.DateTimeField()
	Hiden = models.BooleanField()
