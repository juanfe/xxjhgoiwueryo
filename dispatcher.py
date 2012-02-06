from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
import logging
import urllib

class JsonStore(db.Model):
    content = db.TextProperty()
    
class Bids(db.Model):
    content = db.TextProperty()

class Search(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/search.html",dict))

class MyBids(webapp.RequestHandler):
    def get(self):       
        self.response.out.write(template.render("templates/myBids.html",dict))

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

class Qxapp(webapp.RequestHandler):
    def get(self):
        user = getUser()
        self.response.headers.add_header('Set-Cookie',userCookie())
        if user:
            self.redirect('/system/index.html')
        else:
            self.redirect(users.create_login_url(self.request.uri))

def bidsKey():
    entityKind = 'JsonStore'
    key = getUser()
    return db.Key.from_path(entityKind, key)

def getLatestJsonStore():
    jsonStores = JsonStore.gql("WHERE ANCESTOR IS :1 ", bidsKey())
    jsonStore = None
    for jsonStore in jsonStores:
        logging.info(jsonStore.content)
    return jsonStore

def getLatestJsonStoreContent():
    jsonStore = getLatestJsonStore()
    return jsonStore.content if jsonStore else None

def decodeJsonStr(jsonStr):
    return urllib.unquote(jsonStr.encode('ascii')).decode('utf-8')

class Persist(webapp.RequestHandler):
    def post(self):
        storedJsonStr = getLatestJsonStoreContent()
        if storedJsonStr:
            storedJsonObj = json.loads(storedJsonStr)
        else:
            storedJsonObj = []
        postedJsonStr = self.request.get('bids') 
        postedJsonObj = json.loads(decodeJsonStr(postedJsonStr))
        for element in postedJsonObj:
            storedJsonObj.append(element)
        logging.info(storedJsonObj)
        storedJsonStr = json.dumps(storedJsonObj)
        logging.info(storedJsonStr)
        jsonStore = getLatestJsonStore()
        if (not jsonStore):
            jsonStore = JsonStore(parent=bidsKey())
        jsonStore.content = db.Text(storedJsonStr)
        jsonStore.put()
            
class Retrieve(webapp.RequestHandler):
    def get(self):
        self.response.out.write(getLatestJsonStoreContent())

class Logout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/qxapp'))

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

class DojoBids(webapp.RequestHandler):
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

class DojoLogin(webapp.RequestHandler):
    def get(self):
        user = getUser()
        self.response.headers.add_header('Set-Cookie',userCookie())
        if user:
            self.redirect('/home')
        else:
            self.redirect(users.create_login_url('/'))

class DojoHome(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/home.html",dict))
class DojoLogout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
       
#################################################################

application = webapp.WSGIApplication(
                                     [('/mybids', MyBids),
                                      ('/qxapp', Qxapp),
                                      ('/save', Persist),
                                      ('/bids', Retrieve),
                                      ('/dojobids', DojoBids),
                                      ('/logout', Logout),
                                      ('/home', DojoHome),
                                      ('/dlogout', DojoLogout),
                                      ('/search', Search),
                                      ('/', DojoLogin)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
