from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
import logging
import StringIO
import csv

class Bids(db.Model):
    content = db.TextProperty()

class Search(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/search.html",dict))

class MyBids(webapp.RequestHandler):
    def get(self):       
        self.response.out.write(template.render("templates/mybids.html",dict))

def getUser():
    user = users.get_current_user()
    if user:
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

def clearDbBids():
    bidsQuery = Bids.gql("WHERE ANCESTOR IS :1 ", bidsKey())
    for bids in bidsQuery:
        bids.delete()
    dbBids = None
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
                value['status'] = 'Accepted'
                bidsObj[key] = value
        bidsJson = json.dumps(bidsObj)
        setDbBids(bidsJson)
    def get(self):
        bidsObj = getBidsObj()
        bidsToSendObj = []
        for key, value in bidsObj.iteritems():
            bidsToSendObj.append(value)
        itemsWrapper = {}
        itemsWrapper['items'] = bidsToSendObj
        bidsToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(bidsToSendJson)

class Clean(webapp.RequestHandler):
    def post(self):
        clearDbBids()
        self.redirect('/home')
        
class Login(webapp.RequestHandler):
    def get(self):
        user = getUser()
        #self.response.headers.add_header('Set-Cookie',userCookie())
        if user:
            self.redirect('/home')
        else:
            self.redirect(users.create_login_url('/'))

class Home(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/home.html",dict))
        
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
        self.response.headers['Content-Type'] = 'application/octet-stream'
        self.response.headers['Content-Disposition'] = 'attachment;filename=\"Loans Details.csv\"'
        bidsJson = self.request.get('bids')
        bidsCsv = jsonToCsv(bidsJson)
        #details = getLoansDetails(keys)
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
