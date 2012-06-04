'''
Created on Jun 4, 2012

@authors: Camilo
        Juan Fernando Jaramillo
'''

from google.appengine.ext import db, webapp
from google.appengine.api import users

class User(db.Model):
    account = db.UserProperty(required='true', indexed='false', auto_current_user=True)
    fundsAvailable = db.FloatProperty()
    group = db.StringProperty(#required = 'true',
            choices = ['Admin', 'MO', 'Broker', 'Engine'])
    
def createUser(currUser):
    userEmail = currUser.email()
    user = User.get_by_key_name(key_names = userEmail)
    if user is None:        
        user = User(key_name = userEmail)
        user.fundsAvailable = 0
        user.group = 'Broker'
        user.put()
    
def getCurrentUser(user):
    return User.get_by_key_name(key_names = user.email())

class UserInstance(webapp.RequestHandler):
    def get(self):
        User(key_name = "Admin@test.com",
				account = users.User("Admin@test.com"),
				group = 'Admin').put()
        User(key_name = "Engine@test.com",
				account = users.User("Engine@test.com"),
				group = 'Engine').put()

        User(key_name = "ABCD",
				account = users.User("ABCD@test.com"),
				group = 'MO').put()
        User(key_name = "BCDE",
				account = users.User("BCDE@test.com"),
				group = 'MO').put()
        User(key_name = "EFGH",
				account = users.User("EFGH@test.com"),
				group = 'MO').put()
        User(key_name = "HIJK",
				account = users.User("HIJK@test.com"),
				group = 'MO').put()

        User(key_name = "1104134@test.com", fundsAvailable = 187500.00,
				account = users.User("1104134@test.com"),
                group = 'Broker').put()
        User(key_name = "1104143@test.com", fundsAvailable = 500000.00,
				account = users.User("1104143@test.com"),
                group = 'Broker').put()
        User(key_name = "1104154@test.com", fundsAvailable = 185000.00,
				account = users.User("1104154@test.com"),
                group = 'Broker').put()
        User(key_name = "1104152@test.com", fundsAvailable = 1500000.00,
				account = users.User("1104152@test.com"),
                group = 'Broker').put()
        User(key_name = "1104136@test.com", fundsAvailable = 860000.00,
				account = users.User("1104136@test.com"),
                group = 'Broker').put()
        User(key_name = "1104138@test.com", fundsAvailable = 300000.00,
				account = users.User("1104138@test.com"),
                group = 'Broker').put()
        User(key_name = "1104139@test.com", fundsAvailable = 250000.00,
				account = users.User("1104139@test.com"),
                group = 'Broker').put()
        User(key_name = "1104140@test.com", fundsAvailable = 74000.00,
				account = users.User("1104140@test.com"),
                group = 'Broker') .put()
        User(key_name = "1104141@test.com", fundsAvailable = 285000.00,
				account = users.User("1104141@test.com"),
                group = 'Broker').put()
        User(key_name = "1104159@test.com", fundsAvailable = 532000.00,
				account = users.User("1104159@test.com"),
                group = 'Broker').put()
        User(key_name = "1104161@test.com", fundsAvailable = 292000.00,
				account = users.User("1104161@test.com"),
                group = 'Broker').put()
        User(key_name = "1104145@test.com", fundsAvailable = 752000.00,
				account = users.User("1104145@test.com"),
                group = 'Broker').put()
        User(key_name = "1104133@test.com", fundsAvailable = 418000.00,
				account = users.User("1104133@test.com"),
                group = 'Broker').put()
        User(key_name = "1104149@test.com", fundsAvailable = 47000.00,
				account = users.User("1104149@test.com"),
                group = 'Broker') .put()
        User(key_name = "1104151@test.com", fundsAvailable = 283000.00,
				account = users.User("1104151@test.com"),
                group = 'Broker').put()
        User(key_name = "1104131@test.com", fundsAvailable = 598000.00,
				account = users.User("1104131@test.com"),
                group = 'Broker').put()
        User(key_name = "1104155@test.com", fundsAvailable = 639000.00,
				account = users.User("1104155@test.com"),
                group = 'Broker').put()
        User(key_name = "1104156@test.com", fundsAvailable = 274000.00,
				account = users.User("1104156@test.com"),
                group = 'Broker').put()
        User(key_name = "1104157@test.com", fundsAvailable = 629000.00,
				account = users.User("1104157@test.com"),
                group = 'Broker').put()
        User(key_name = "1104158@test.com", fundsAvailable = 52000.00,
				account = users.User("1104158@test.com"),
                group = 'Broker').put()
