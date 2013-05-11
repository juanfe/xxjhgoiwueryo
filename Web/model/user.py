'''
Created on Feb 21, 2012

@authors: Camilo
        Juan Fernando Jaramillo
'''
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from page import Page, HomePage, LogoutPage, SearchPage, MyBidsPage, CalcPage, UsersPage
import functools


class User(db.Model):
    account = db.UserProperty(required='true', indexed='false',
            auto_current_user=True)
    fundsAvailable = db.FloatProperty()
    group = db.StringProperty(  # required = 'true',
            choices = ['Admin', 'MO', 'Broker', 'Engine', 'Guest', 'Demo'])


def createUser(currUser):
    userEmail = currUser.email()
    user = User.get_by_key_name(key_names = userEmail)
    if user is None:
        user = User(key_name = userEmail)
        # TODO as soon it official change to funds 0 and group Guest
        user.fundsAvailable = 1000000.0
        user.group = 'Broker'
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
    return User.get_by_key_name(key_names = key_name)


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
                    page = Page.NOTALLOW
                    parameters = getPageDict(page)
                    self._obj.response.out.write(template.render(
                            "templates/notallowed.html", parameters))
    return _PageAllowed


def getMenuPages(page):
    enumRegister = {
        Page.HOME: HomePage,
        Page.SEARCH: SearchPage,
        Page.MYBIDS: MyBidsPage,
        Page.CALC: CalcPage,
        Page.LOGOUT: LogoutPage,
        Page.USERS: UsersPage
    }
    menuPages = []
    for key, val in enumRegister.iteritems():
        if key != page and getGroup() in val.groups:
            menuPages.append(val)
    return menuPages


def getPageDict(page):
    return {
        'menuPages': getMenuPages(page)
    }
