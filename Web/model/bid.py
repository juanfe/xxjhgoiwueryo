'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db, webapp
from google.appengine.api import users
from user import User, getUser
from model.loan import Loan, getLoan
import datetime
import time

class Bid(db.Model):
    user = db.ReferenceProperty(User, verbose_name="User", collection_name = 'bids', required = 'true')
    #bidtype = db.StringProperty(verbose_name="Bid Type", choices = ['General',
    #        'Specified'], required = 'true')
    bidtype = db.StringProperty(verbose_name="Bid Type", choices = ['General', 'Specified'])
    loan = db.ReferenceProperty(Loan, verbose_name="Loan", collection_name = 'bids')
    participation = db.FloatProperty(verbose_name="Participation %", required = 'true')
    lorm = db.StringProperty(verbose_name="Loan or MO", choices = ['Loan', 'MO'])
    mo = db.ReferenceProperty(User, verbose_name="Mortgage Originator")
    aggregated = db.FloatProperty(verbose_name="if general: Aggregate $")
    bidrate = db.FloatProperty(verbose_name="Bid rate")
    status = db.StringProperty(verbose_name="Status", choices = ['Accepted', 'Active', 'Cancelled'])
    ordertype = db.StringProperty(verbose_name="Order Type", choices =
    		#['Noncompetitive', 'Competitive'], required = 'true')
    		['Noncompetitive', 'Competitive'])
    ordertiming = db.StringProperty(verbose_name="Order Timing", choices =
            ['Auto', 'Day Trade'])
            #['Auto', 'Day Trade'], required = 'true')
    createdAt = db.DateTimeProperty(verbose_name="Created at")
    expiresAt = db.DateTimeProperty(verbose_name="Expires at")
    orderAt = db.DateTimeProperty(verbose_name="Order placed at")
