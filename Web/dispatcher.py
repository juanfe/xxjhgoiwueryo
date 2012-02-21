from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
import logging
import StringIO
import csv
import random
from datetime import datetime
from datetime import timedelta
from ls.model.user import User
from ls.model.bid import Bid
from ls.model.simpleLoan import SimpleLoan

#Model for storage
class Bids(db.Model):
    content = db.TextProperty()

#Rendering logic
class Page:
    HOME = 1
    SEARCH = 2
    MYBIDS = 3
    LOGOUT = 4
    
class HomePage:
    url = "'/home'"
    text = 'Home'
class SearchPage:
    url = "'/search'"
    text = 'Search assets'
class MyBidsPage:
    url = "'/mybids'"
    text = 'My bids'
class LogoutPage:
    url = "'/logout'"
    text = 'Logout'
def getMenuPages(page):
    enumRegister = {
        Page.HOME : HomePage,
        Page.SEARCH : SearchPage,
        Page.MYBIDS : MyBidsPage,
        Page.LOGOUT : LogoutPage
    }
    menuPages = []
    for key,val in enumRegister.iteritems():
        if key != page:
            menuPages.append(val)
    return menuPages
def getPageDict(page):
    return {
            'menuPages' : getMenuPages(page)
    }
#Rendered pages
def checkLogin(requestHandler):
    if (not getUser()):
        requestHandler.redirect('/')
    requestHandler.response.headers['Cache-Control'] = 'no-store, no-cache'
    requestHandler.response.headers['Pragma'] = 'no-cache'
    requestHandler.response.headers['Expires'] = '-1'

class Home(webapp.RequestHandler):
    def get(self):
        checkLogin(self)
        page = Page.HOME
        parameters = getPageDict(page)
        parameters = None
        self.response.out.write(template.render("templates/home.html",parameters))

class Search(webapp.RequestHandler):
    def get(self):
        checkLogin(self)
        page = Page.SEARCH
        parameters = getPageDict(page)
        parameters = None
        self.response.out.write(template.render("templates/search.html",parameters))

class MyBids(webapp.RequestHandler):
    def get(self):
        checkLogin(self) 
        page = Page.MYBIDS
        parameters = getPageDict(page)
        parameters = None
        self.response.out.write(template.render("templates/mybids.html",parameters))

#Retrieving the current logged user
def getUser():
    user = users.get_current_user()
    if user:
        userEmail = user.email()
        dbUser = User.get_by_key_name(userEmail)
        if(not dbUser):
            dbUser = User(key_name = userEmail, account = user)
            dbUser.put()
        return users.get_current_user().email()
    else:
        return None

def userCookie():
    userCookieKey = 'com.liquidityspot.user'
    user = getUser()
    if user:
        return '%s=%s;' % (userCookieKey, user)
    else:
        return '%s=; Max-Age=0; Path=/' % userCookieKey

def bidsKey():
    entityKind = 'Bids'
    key = getUser()
    return db.Key.from_path(entityKind, key)

#Storage of the dojo bids json
dojoAjaxKey = 'bids'
def getDbBids():
    bidsQuery = Bids.gql("WHERE ANCESTOR IS :1 ", bidsKey())
    dbBids = None
    for bids in bidsQuery:
        dbBids = bids
    return dbBids

def getBidsObj():
    bids =  getDbBids()
    if bids:
        bidsJson = bids.content
        bidsObj = json.loads(bidsJson)
    else:
        bidsObj = {}
    return bidsObj

def getBidsJson():
    bidsObj = getBidsObj()
    return json.dumps(bidsObj)

def setDbBids(bidsJson):
    bids =  getDbBids()
    if (not bids):
        bids = Bids(parent=bidsKey())
    bids.content = bidsJson
    bids.put()        

class BidsRest(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        bidsObj = getBidsObj()
        bidsToAddJson = self.request.get('bids')
        bidsToAddObj =  json.loads(bidsToAddJson)
        for key, value in bidsToAddObj.iteritems():
            if key in bidsObj:
                bidData =  bidsObj[key]
                bidData['participation'] = value['participation']
                bidData['bidrate'] = value['bidrate']
                bidsObj[key] = bidData
            else:
                possibleStatuses = ['Accepted', 'Active', 'Cancelled']
                value['status'] = possibleStatuses[random.randint(0,2)]
                creationTime = datetime.now()
                value['createdAt'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                expirationTime = creationTime + timedelta(hours=2)
                value['expiresAt'] = expirationTime.strftime('%Y/%m/%d %H:%M:%S')
                bidsObj[key] = value
        bidsJson = json.dumps(bidsObj)
        setDbBids(bidsJson)
    def get(self):
        checkLogin(self)
        bidsObj = getBidsObj()
        bidsToSendObj = []
        for value in bidsObj.itervalues():
            bidsToSendObj.append(value)
        itemsWrapper = {}
        itemsWrapper['items'] = bidsToSendObj
        bidsToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(bidsToSendJson)

class Clean(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        bidsObj = getBidsObj()
        bidsToDeleteJson = self.request.get('bids')
        bidsToDeleteObj =  json.loads(bidsToDeleteJson)
        for key in bidsToDeleteObj.iterkeys():
            if key in bidsObj:
                bidsObj.pop(key)
        bidsJson = json.dumps(bidsObj)
        bids =  getDbBids()
        if (bids):
            bids.content = bidsJson
            bids.put()

class Login(webapp.RequestHandler):
    def get(self):
        user = getUser()
        #self.response.headers.add_header('Set-Cookie',userCookie())
        if user:
            self.redirect('/home')
        else:
            self.redirect(users.create_login_url('/'))

class Logout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
        
def jsonToCsv(jsonStr):
    rows = json.loads(jsonStr)
    csvOut = StringIO.StringIO()
    if rows is not None:
        writer = csv.writer(csvOut)
        writer.writerows(rows)
    csvStr = csvOut.getvalue()
    csvOut.close()
    return csvStr
    
class Download(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        self.response.headers['Content-Type'] = 'application/octet-stream'
        self.response.headers['Content-Disposition'] = 'attachment;filename=\"Loans Details.csv\"'
        bidsJson = self.request.get('bids')
        bidsCsv = jsonToCsv(bidsJson)
        self.response.out.write(bidsCsv)
        
       
#################################################################

application = webapp.WSGIApplication(
                                     [('/mybids', MyBids),
                                      ('/bids', BidsRest),
                                      ('/home', Home),
                                      ('/logout', Logout),
                                      ('/search', Search),
                                      ('/clean', Clean),
                                      ('/download', Download),
                                      ('/', Login)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
