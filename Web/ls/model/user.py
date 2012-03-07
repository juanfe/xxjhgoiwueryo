'''
Created on Feb 21, 2012

@author: Camilo
'''

import random

from google.appengine.ext import db

class User(db.Model):
    account = db.UserProperty(required='true', indexed='false', auto_current_user=True)
    fundsAvailable = db.IntegerProperty()
    
def createUser(currUser):
    userEmail = currUser.email()
    user = User.get_by_key_name(key_names = userEmail)
    if user is None:        
        user = User(key_name = userEmail)
        user.fundsAvailable = random.randint(100,1000) * 1000
        user.put()
    
def getCurrentUser(user):
    return User.get_by_key_name(key_names = user.email())