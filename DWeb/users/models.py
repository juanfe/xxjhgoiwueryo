import moneyed
#from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.db import models

class FundsCashFlow(models.Model):
	User = models.ForeignKey(User)
	#Funds = MoneyField(max_digits = 20, decimal_places = 9,
	#		default_currency = moneyed.USD)
	#FundsDate = models.DateTimeField(auto_now = True)
	Funds = models.FloatField(verbose_name = "Funds Available")
