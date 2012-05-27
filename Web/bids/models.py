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
    ExpiresAt = models.DateTimeField(auto_now = True, null = True)
    Type = models.CharField(max_length = 1, choices = TYPE_CHOICES)
    #Aggregated = MoneyField(max_digits = 20, decimal_places = 9,
    #            default_currency = moneyed.USD)
    Aggregated = models.FloatField(verbose_name="Aggregate $", null = True)
    #AggregatedDate = models.DateTimeField(auto_now = True, null = True)
    Participation = models.DecimalField(max_digits = 13, decimal_places = 9,
            verbose_name = "Participation", null = True)
    LoanType = models.CharField(max_length = 1, choices = LOAN_CHOICES,
            verbose_name = "Loan Type", null = True)
    Competitive = models.BooleanField(verbose_name = "Is Competitive")
    CompetitiveBidRate = models.DecimalField(max_digits = 13, decimal_places = 9,
            null = True)
    OrderTiming = models.CharField(max_length = 1, choices = ORDER_CHOICES,
            verbose_name = "Order Timing")
    #FundsAvailable = MoneyField(max_digits = 20, decimal_places = 9,
    #            default_currency = moneyed.USD)
    FundsAvailable = models.FloatField(verbose_name = "Funds Available")
    #FundsAvailableDate = models.DateTimeField(auto_now = True)
    Status = models.CharField(max_length = 1, choices = STATUS_CHOICES,
            verbose_name = "Status", null = True)

    def __unicode__(self):
        return self.User
