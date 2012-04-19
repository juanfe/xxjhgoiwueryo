#!/usr/bin/env python
from django.core.management import setup_environ
from django.contrib.auth.models import User
from bids.models import Bid
from loans.models import Loan, MortgageOriginator
from users.models import FundsCashFlow
import settings

setup_environ(settings)

#Creating MO
user = User.objects.create_user('ABC Mortgage', 'ABC_Mortgage@tempo.com',
		'1234')
user.is_staff = True
user.save()

user = User.objects.create_user('Prime Lending', 'Prime_Lending@tempo.com',
		'1234')
user.is_staff = True
user.save()

user = User.objects.create_user('Best Loans Inc', 'Best_Loans_Inc@tempo.com',
		'1234')
user.is_staff = True
user.save()

user = User.objects.create_user('Integrity Lending', 'Integrity_Lending@tempo.com',
		'1234')
user.is_staff = True
user.save()

