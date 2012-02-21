'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db

class SimpleLoan(db.Model):
    collateral_key = db.IntegerProperty(
                        verbose_name = "Loan Number",
                        name = "collateral_key",
                        required = True)
    state = db.StringProperty(
                        verbose_name = "Property state",
                        name = "state",
                        required = True)
    curr_upb = db.IntegerProperty(
                        verbose_name = "Current Unpaid Balance",
                        name = "curr_upb",
                        required = True)