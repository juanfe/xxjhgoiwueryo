'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db

class User(db.Model):
    account = db.UserProperty(required='true', indexed='false')
    
def createUser(user):
    User(key_name = user.email(), account = user).put()
    
def getCurrentUser(user):
    return User.get_by_key_name(key_names = user.email())
    #return User.get_by_key_name(key_name = user.email())