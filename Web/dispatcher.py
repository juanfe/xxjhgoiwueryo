from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
import StringIO, csv, random, logging
from datetime import datetime, timedelta
from ls.model import user
from ls.model.bid import Bid
from ls.model.simpleLoan import SimpleLoan

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
    curr_user = users.get_current_user()
    if curr_user:
        user.createUser(curr_user)
        return curr_user.email()
    else:
        return None

def bidsKey():
    entityKind = 'Bids'
    key = getUser()
    return db.Key.from_path(entityKind, key)

#Storage of the dojo bids json
dojoAjaxKey = 'bids'
class BidsRest(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        bidsToAddJson = self.request.get('bids')
        bidsToAddObj =  json.loads(bidsToAddJson)
        # Adding the bid model objects
        dbUser = user.getCurrentUser(users.get_current_user())
        for key, value in bidsToAddObj.iteritems():
            gqlQuery = Bid.gql("WHERE ANCESTOR IS KEY('User', :email) AND loan= Key('SimpleLoan',:collateral)",
                                email= getUser(), collateral= key)
            bid = gqlQuery.get()
            participation = float(value['participation'])
            bidrate = float(value['bidrate'])
            statusChoices = Bid.status.choices
            status = statusChoices[random.randint(0,len(statusChoices)-1)]
            creationTime = datetime.now()
            expirationTime = creationTime + timedelta(hours=2)
            if(not bid):
                loan = SimpleLoan(key_name= str(key), collateral_key = key)
                loan.put()
                Bid(parent = dbUser,
                          user = dbUser,
                          loan = loan,
                          participation = participation,
                          bidrate = bidrate,
                          status = status,
                          createdAt = creationTime,
                          expiresAt = expirationTime).put()
            else:
                bid.participation = participation
                bid.bidrate = bidrate
                bid.put()
    def get(self):
        checkLogin(self)
        # Getting bids from the Db
        bidsModelObj = []
        modelBids = user.getCurrentUser(users.get_current_user()).bids
        for modelBid in modelBids:
            bidModelObj = {}
            bidModelObj['collateral_key'] = modelBid.loan.collateral_key
            bidModelObj['participation'] = modelBid.participation
            bidModelObj['bidrate'] = modelBid.bidrate
            bidModelObj['status'] = modelBid.status
            bidModelObj['createdAt'] = modelBid.createdAt.strftime('%Y/%m/%d %H:%M:%S')
            bidModelObj['expiresAt'] = modelBid.expiresAt.strftime('%Y/%m/%d %H:%M:%S')
            bidsModelObj.append(bidModelObj)
        # Wrapping and sending
        itemsWrapper = {}
        itemsWrapper['items'] = bidsModelObj
        bidsToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(bidsToSendJson)

class Clean(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        bidsToDeleteJson = self.request.get('bids')
        bidsToDeleteObj =  json.loads(bidsToDeleteJson)
        # Deleting bid model
        for key in bidsToDeleteObj.iterkeys():
            gqlQuery = Bid.gql("WHERE ANCESTOR IS KEY('User', :email) AND loan= Key('SimpleLoan',:collateral)",
                                email= getUser(), collateral= key)
            bid = gqlQuery.get()
            if(bid):
                bid.delete()
        

class Login(webapp.RequestHandler):
    def get(self):
        user = getUser()
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
