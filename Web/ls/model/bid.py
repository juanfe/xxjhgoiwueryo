'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db
from ..model.user import User
from ..model.simpleLoan import SimpleLoan

class Bid(db.Model):
    user = db.ReferenceProperty(User, collection_name = 'bids', required = 'true')
    loan = db.ReferenceProperty(SimpleLoan, collection_name = 'bids', required = 'true')
    participation = db.FloatProperty(required = 'true')
    bidrate = db.FloatProperty(required = 'true')
    status = db.StringProperty(choices = ['Accepted', 'Active', 'Cancelled'])
    createdAt = db.DateTimeProperty()
    expiresAt = db.DateTimeProperty()