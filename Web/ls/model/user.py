'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db

class User(db.Model):
    account = db.UserProperty(required='true', indexed='false')