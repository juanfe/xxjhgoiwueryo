'''
Created on Feb 21, 2012

@authors: Camilo
        Juan Fernando Jaramillo
'''
from google.appengine.api import users
from google.appengine.ext import webapp
from user import PageAllowed
from user import User


class DeleteUsers(webapp.RequestHandler):    
    @PageAllowed(['Demo',])
    def get(self):
        gql_object = db.GqlQuery("SELECT * FROM User")
        for item in gql_object: 
            item.delete()  


class UsrInstance():
    def UpdateDemoData(self):
        self.get_demo()

    def get(self):
        User(key_name = "john.duhadway@liquidityspot.com",
                account = users.User("john.duhadway@liquidityspot.com"),
                group = 'Demo').put()
        User(key_name = "john@duhadwayllc.com",
                account = users.User("john@duhadwayllc.com"),
                group = 'Demo').put()
        User(key_name = "marscamand@gmail.com",
                account = users.User("marscamand@gmail.com"),
                group = 'Demo').put()
        User(key_name = "leonardo.zuniga@gmail.com", fundsAvailable = 1000000.0,
                account = users.User("leonardo.zuniga@gmail.com"),
                group = 'Demo').put()
        User(key_name = "michaelhow@gmail.com", fundsAvailable = 1000000.0,
                account = users.User("michaelhow@gmail.com"),
                group = 'Demo').put()
        User(key_name = "paola.chikung@gmail.com", fundsAvailable = 1000000.0,
                account = users.User("paola.chikung@gmail.com"),
                group = 'Demo').put()

        User(key_name = "juajarastar@gmail.com",
                account = users.User("juajarastar@gmail.com"),
                group = 'Admin').put()
        User(key_name = "Admin@test.com",
                account = users.User("Admin@test.com"),
                group = 'Admin').put()
        User(key_name = "Engine@test.com",
                account = users.User("Engine@test.com"),
                group = 'Engine').put()

        User(key_name = "ABCD@test.com",
                account = users.User("ABCD@test.com"),
                group = 'MO').put()
        User(key_name = "BCDE@test.com",
                account = users.User("BCDE@test.com"),
                group = 'MO').put()
        User(key_name = "EFGH@test.com",
                account = users.User("EFGH@test.com"),
                group = 'MO').put()
        User(key_name = "HIJK@test.com",
                account = users.User("HIJK@test.com"),
                group = 'MO').put()

    def get_demo(self):
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
        User(key_name = "1104158@test.com", fundsAvailable = 1052000.00,
                account = users.User("1104158@test.com"),
                group = 'Broker').put()
