'''
Created on Feb 21, 2012

@authors: Camilo
        Juan Fernando Jaramillo
'''

from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
import functools


class User(db.Model):
    account = db.UserProperty(required='true', indexed='false',
            auto_current_user=True)
    fundsAvailable = db.FloatProperty()
    group = db.StringProperty(  # required = 'true',
            choices = ['Admin', 'MO', 'Broker', 'Engine', 'Guest'])


def createUser(currUser):
    userEmail = currUser.email()
    user = User.get_by_key_name(key_names = userEmail)
    if user is None:
        user = User(key_name = userEmail)
        user.fundsAvailable = 0.0
        user.group = 'Guest'
        user.put()


# Get the db user, using the system user
# get the db user from the system user
# Sample
# u = users.get_current_user()
# print (user.getTheUser(u).account)
# >>> juajarastar
def getTheUser(user):
    if user == None:
        return user
    try:
        email = user.email()
    except:
        email = str(user)
    return User.get_by_key_name(key_names = email)


# Get the db user from the db using the mail = key name
# Sample: print (user.getUser("1104134@test.com").account)
# >>> 1104134@test.com
def getUser(key_name):
    return db.get(db.Key.from_path("User", key_name))


# Get the current user key name = email, or None if there are not
def getCurrentUser():
    u = users.get_current_user()
    if u:
        return u.email()
    else:
        return u


def getGroup():
    u = getCurrentUser()
    if u:
        w = User.get_by_key_name(key_names = u)
        if w:
            return w.group
        else:
            return w
    else:
        return u


def PageAllowed(groups):
    class _PageAllowed(object):
        def __init__(self, func):
            self.func = func

        def __get__(self, obj, type = None):
            self._obj = obj
            return functools.partial(self, obj)

        def __call__(self, *args, **kw):
            u = users.get_current_user()
            # If not connected
            if u == None:
                self._obj.redirect(users.create_login_url('/'))
            else:
                dbUser = getTheUser(u) 
                # If the user is not in the db
                if not dbUser:
                    createUser(u)
                g = getGroup()
                if g in groups:
                    self.func(*args, **kw)
                else:
                    self._obj.response.out.write(template.render(
                            "templates/notallowed.html", []))
    return _PageAllowed


class UserInstance(webapp.RequestHandler):
    def get(self):
        User(key_name = "john.duhadway@liquidityspot.com",
                account = users.User("john.duhadway@liquidityspot.com"),
                group = 'Broker').put()
        User(key_name = "john@duhadwayllc.com",
                account = users.User("john@duhadwayllc.com"),
                group = 'Broker').put()
        User(key_name = "marscamand@gmail.com",
                account = users.User("marscamand@gmail.com"),
                group = 'Broker').put()

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
