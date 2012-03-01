'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db
from ..model.user import User
from model.loansModel import loansModel

class Bid(db.Model):
    user = db.ReferenceProperty(User, verbose_name="User", collection_name = 'bids', required = 'true')
    loan = db.ReferenceProperty(loansModel, verbose_name="Loan", collection_name = 'bids', required = 'true')
    participation = db.FloatProperty(verbose_name="Participation %", required = 'true')
    bidrate = db.FloatProperty(verbose_name="Bid rate", required = 'true')
    status = db.StringProperty(verbose_name="Status", choices = ['Accepted', 'Active', 'Cancelled'])
    createdAt = db.DateTimeProperty(verbose_name="Created at")
    expiresAt = db.DateTimeProperty(verbose_name="Expires at")