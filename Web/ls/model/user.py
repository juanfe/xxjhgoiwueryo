'''
Created on Feb 21, 2012

@author: Camilo
'''

from google.appengine.ext import db

class User(db.Model):
    account = db.UserProperty(required='true', indexed='false')
    
def createUser(user):
    userEmail = user.email()
    dbUser = User.get_by_key_name(userEmail)
    if(not dbUser):
        dbUser = User(key_name = userEmail, account = user)
        dbUser.put()