from google.appengine.api import users, memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
import StringIO, csv, random, logging
from datetime import datetime, timedelta, date
from ls.model import user, bid 
from ls.model.bid import Bid
from ls.model.user import User 
from ls.model.user import PageAllowed, getGroup
from model import loansModel
from calc import calc

#Rendering logic
class Page:
    HOME = 1
    SEARCH = 2
    CALC = 3
    MYBIDS = 4
    LOGOUT = 5
    USERS = 6
    
class HomePage:
    url = "'/home'"
    text = 'Home'
    groups = ['Admin', 'MO', 'Broker', 'Engine', 'Guest']
class SearchPage:
    url = "'/search'"
    text = 'Search loans'
    groups = ['Admin', 'MO', 'Broker', 'Guest']
class CalcPage:
    url = "'/calc'"
    text = 'Calculate'
    groups = ['Admin', 'Engine']
class MyBidsPage:
    url = "'/mybids'"
    text = 'My bids'
    groups = ['Admin', 'MO', 'Broker']
class LogoutPage:
    url = "'/logout'"
    text = 'Logout'
    groups = ['Admin', 'MO', 'Broker', 'Engine', 'Guest']
class UsersPage:
    url = "'/manusers'"
    text = 'Users'
    groups = ['Admin']
def getMenuPages(page):
    enumRegister = {
        Page.HOME : HomePage,
        Page.SEARCH : SearchPage,
        Page.MYBIDS : MyBidsPage,
        Page.CALC : CalcPage,
        Page.LOGOUT : LogoutPage,
        Page.USERS : UsersPage
    }
    menuPages = []
    for key,val in enumRegister.iteritems():
        if key != page and getGroup() in val.groups:
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
    @PageAllowed(['Admin', 'Broker', 'MO', ])
    def get(self):
        checkLogin(self)
        page = Page.HOME
        parameters = getPageDict(page)
        parameters['User'] = user.getCurrentUser()
        self.response.out.write(template.render("templates/home.html",parameters))

class Search(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker'])
    def get(self):
        checkLogin(self)
        page = Page.SEARCH
        parameters = getPageDict(page)
        parameters['User'] = user.getCurrentUser()
        self.response.out.write(template.render("templates/search.html",parameters))

class Calc(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Engine'])
    def get(self):
        checkLogin(self)
        page = Page.CALC
        parameters = getPageDict(page)
        parameters['User'] = user.getCurrentUser()
        c = calc()
        if c.has_key('loans') and c.has_key('bids'):
            parameters['loans'] = c['loans']
            parameters['bids'] = c['bids']
        self.response.out.write(template.render("templates/results.html",parameters))

class MyBids(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker'])
    def get(self):
        checkLogin(self) 
        page = Page.MYBIDS
        parameters = getPageDict(page)
        parameters['User'] = user.getCurrentUser()
        self.response.out.write(template.render("templates/mybids.html",parameters))

class Users(webapp.RequestHandler):
    @PageAllowed(['Admin'])
    def get(self):
        checkLogin(self)
        page = Page.USERS
        parameters = getPageDict(page)
        parameters['User'] = user.getCurrentUser()
        self.response.out.write(template.render("templates/users.html",parameters))

#Retrieving the current logged user
def getUser():
    curr_user = users.get_current_user()
    if curr_user:
        user.createUser(curr_user)
        return curr_user.email()
    else:
        return None

#Storage of the dojo bids json
dojoAjaxKey = 'bids'
class BidsRest(webapp.RequestHandler):
    def post(self):
        checkLogin(self)
        bidsToAddJson = self.request.get(dojoAjaxKey)
        bidsToAddObj =  json.loads(bidsToAddJson)
        # Adding the bid model objects
        dbUser = user.getTheUser(users.get_current_user())
        # Getting the bids for the current user
        userBids = dbUser.bids
        currentBids = {}
        #TODO if the user is an admin, then add all the bids
        #TODO if the user is a MO, the add the users for the MO
        for bid in userBids:
            currentBids[bid.loan.collateral_key] = bid
        currentBidsKeys = currentBids.keys()
        # Adding or updating the bids
        statusChoices = Bid.status.choices
        creationTime = datetime.now()
        expirationTime = creationTime + timedelta(hours=2)
        for key, value in bidsToAddObj.iteritems():
            # Getting user input values
            participation = float(value['participation'])
            bidrate = float(value['bidrate'])
            # Checking if there is a bid for a given collateral key
            if (key in currentBidsKeys):
                bid = currentBids[key]
                bid.participation = participation
                bid.bidrate = bidrate
                bid.put()
            else:
                loanQuery = loansModel.loansModel.all().filter('collateral_key =', key)
                loan = loanQuery.get()
                #TODO check why the status is random?
                #status = random.choice(statusChoices)
                status = 'Active'
                Bid(parent = dbUser,
                          user = dbUser,
                          loan = loan,
                          participation = participation,
                          bidrate = bidrate,
                          #TODO add the posibility of get a None value in
                          # bidrate, it is in the myscript.js
                          ordertype = 'Competitive' if bidrate != None else 'Noncompetitive',
                          status = status,
                          createdAt = creationTime,
                          expiresAt = expirationTime,
                          #Added to agree with the LiqSpop engine
                          #TODO is better to put it on the web
                          bidtype = 'Specified',
                          lorm = 'Loan',
                          ordertiming = 'Day Trade',
                          key_name = "%s %s"%(user.getCurrentUser(), creationTime),
                          ).put()
    def get(self):
        checkLogin(self)
        # Getting bids from the Db
        bidsModelObj = []
        modelBids = user.getTheUser(users.get_current_user()).bids
        #TODO add the new fields
        for modelBid in modelBids:
            bidModelObj = {}
            #FIXME if there are no necesarilly collateral_key 
            #CHECK the next line
            #if modelBid.loan == None: #or the next line
            #if modelBid.loan:
            bidModelObj['collateral_key'] = modelBid.loan.collateral_key
            #else:
            #    bidModelObj['collateral_key'] = "" 
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
    def delete(self):
        checkLogin(self)
        bidsToDeleteJson = self.request.get(dojoAjaxKey)
        bidsToDeleteObj =  json.loads(bidsToDeleteJson)
        userBids = user.getTheUser(users.get_current_user()).bids
        currentBids = {}
        for bid in userBids:
            currentBids[bid.loan.collateral_key] = bid
        currentBidsKeys = currentBids.keys()            
        # Deleting bid model
        for key in bidsToDeleteObj.iterkeys():
            if(key in currentBidsKeys):
                currentBids.pop(key).delete()
                currentBidsKeys = currentBids.keys()

#Storage of the dojo bids json
dojoAjaxKey = 'bids'
class UsersRest(webapp.RequestHandler):
    #def post(self):
    #    checkLogin(self)
    #    usersToAddJson = self.request.get(dojoAjaxKey)
    #    usersToAddObj =  json.loads(usersToAddJson)
    #    # Adding the bid model objects
    #    ##dbUser = user.getTheUser(users.get_current_user())
    #    # Getting the bids for the current user
    #    userBids = dbUser.bids
    #    currentBids = {}
    #    for bid in userBids:
    #        currentBids[bid.loan.collateral_key] = bid
    #    currentBidsKeys = currentBids.keys()
    #    # Adding or updating the bids
    #    statusChoices = Bid.status.choices
    #    creationTime = datetime.now()
    #    expirationTime = creationTime + timedelta(hours=2)
    #    for key, value in usersToAddObj.iteritems():
    #        # Getting user input values
    #        participation = float(value['participation'])
    #        bidrate = float(value['bidrate'])
    #        # Checking if there is a bid for a given collateral key
    #        if (key in currentBidsKeys):
    #            bid = currentBids[key]
    #            bid.participation = participation
    #            bid.bidrate = bidrate
    #            bid.put()
    #        else:
    #            loanQuery = loansModel.loansModel.all().filter('collateral_key =', key)
    #            loan = loanQuery.get()
    #            #TODO check why the status is random?
    #            #status = random.choice(statusChoices)
    #            status = 'Active'
    #            Bid(parent = dbUser,
    #                      user = dbUser,
    #                      loan = loan,
    #                      participation = participation,
    #                      bidrate = bidrate,
    #                      #TODO add the posibility of get a None value in
    #                      # bidrate, it is in the myscript.js
    #                      ordertype = 'Competitive' if bidrate != None else 'Noncompetitive',
    #                      status = status,
    #                      createdAt = creationTime,
    #                      expiresAt = expirationTime,
    #                      #Added to agree with the LiqSpop engine
    #                      #TODO is better to put it on the web
    #                      bidtype = 'Specified',
    #                      lorm = 'Loan',
    #                      ordertiming = 'Day Trade',
    #                      key_name = "%s %s"%(user.getCurrentUser(), creationTime),
    #                      ).put()

    def get(self):
        checkLogin(self)
        # Getting bids from the Db
        usersModelObj = []
        modelUsers = Bid.all()#User.all() #Bid.all()
        for modelUser in modelUsers:
            userModelObj = {}
            #userModelObj['fundsAvailable'] = modelUser.fundsAvailable
            userModelObj['collateral_key'] = "" #modelUser.loan.collateral_key
            userModelObj['participation'] = modelUser.participation
            usersModelObj.append(userModelObj)
        # Wrapping and sending
        itemsWrapper = {}
        itemsWrapper['items'] = usersModelObj
        usersToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(usersToSendJson)
    #def delete(self):
    #    checkLogin(self)
    #    bidsToDeleteJson = self.request.get(dojoAjaxKey)
    #    bidsToDeleteObj =  json.loads(bidsToDeleteJson)
    #    userBids = user.getTheUser(users.get_current_user()).bids
    #    currentBids = {}
    #    for bid in userBids:
    #        currentBids[bid.loan.collateral_key] = bid
    #    currentBidsKeys = currentBids.keys()            
    #    # Deleting bid model
    #    for key in bidsToDeleteObj.iterkeys():
    #        if(key in currentBidsKeys):
    #            currentBids.pop(key).delete()
    #            currentBidsKeys = currentBids.keys()

class jsonLoans(webapp.RequestHandler):
    def get(self):
        checkLogin(self)
        bidsToSendJson = memcache.get("bidsToSendJson")
        if bidsToSendJson is None:
            bidsToSendJson = self.generateLoans()
            if not memcache.add("bidsToSendJson", bidsToSendJson, 3600):
                logging.error("Memcache set failed.")
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(bidsToSendJson)
    def generateLoans(self):
        loanJsonObj = []
        datetypeObj = date.today()
        nonetypeObj = None
        loans = loansModel.loansModel.all()
        for loan in loans:
            loanObj = {}
            for k, v in vars(loan).items():
                k = k[1:]
                if k != 'entity' and k != 'from_entity':
                    if type(v)==type(datetypeObj):
                        loanObj[k] = '{0}/{1}/{2}'.format(v.month,v.day,v.year) #strftime('%m/%d/%Y')
                    elif type(v) == bool:
                        loanObj[k] = 1 if v else 0
                    elif type(v)==type(nonetypeObj):
                        loanObj[k] = ''
                    else:
                        loanObj[k] = v
#                    self.response.out.write('{0}({1}) {2}\n'.format(k,type(loanObj[k]),loanObj[k]))
#            self.response.out.write('\n\n')
            loanJsonObj.append(loanObj)
        itemsWrapper = {}
        itemsWrapper['items'] = loanJsonObj
        return json.dumps(itemsWrapper)
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
        bidsJson = self.request.get(dojoAjaxKey)
        bidsCsv = jsonToCsv(bidsJson)
        self.response.out.write(bidsCsv)

class Labels(webapp.RequestHandler):
    def get(self):
        fieldToLabelDict = {}
        # models where the labels are defined as verbose names
        models = [ loansModel.loansModel, Bid ]
        for model in models:
            fieldToLabelDict.update(self.getModelPropertiesFieldToVerboseNameDict(model))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(fieldToLabelDict))
        
    def getModelPropertiesFieldToVerboseNameDict(self, model):
        propertiesFieldToVerboseNamesDict = {}
        for field, modelProperty in model.properties().iteritems():
            propertiesFieldToVerboseNamesDict[field] = modelProperty.verbose_name
        return propertiesFieldToVerboseNamesDict

class BidWindow():
    class Bids(webapp.RequestHandler):
        def get(self):
            bidsObj = {}
            for bid in Bid.all():
                bidObj = {}
                # Extracting properties
                bidId = bid.key().id_or_name()
                time = bid.createdAt.strftime("%H:%M:%S")
                date = bid.createdAt.strftime("%Y-%m-%d")
                participation = bid.participation
                loanId = bid.loan.key().id_or_name()
                bidRate = bid.bidrate
                orderType = 'Competitive' if (bidRate > 0) else 'Noncompetitive'
                userId = bid.user.key().id_or_name()
                # Passing properties to the obj
                bidObj['bidId'] = bidId
                bidObj['date'] = date
                bidObj['time'] = time
                bidObj['bidType'] = 'Specified'
                bidObj['participation'] = participation
                bidObj['assetSubset'] = 'Loan'
                bidObj['loanId'] = loanId
                bidObj['orderType'] = orderType
                if (orderType == 'Competitive'):
                    bidObj['bidRate'] = bidRate
                bidObj['orderTiming'] = 'Day Trade'
                bidObj['userId'] = userId
                # Inserting new object into the accumulation object
                bidsObj[bidId] = bidObj
            # Dumping to JSON the accumulation object
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(bidsObj))
            
    class Loans(webapp.RequestHandler):
        def get(self):
            loansObj = {}
            for bid in Bid.all():
                loan = bid.loan
                loanId = loan.key().id_or_name()
                if (loanId not in loansObj):
                    loanObj = {}
                    # Extracting properties
                    mo = loan.customer_account_key
                    loanAmount = loan.curr_upb
                    # Passing properties to the obj
                    loanObj['loanId'] = loanId
                    loanObj['mortgageOriginator'] = mo
                    loanObj['loanAmount'] = loanAmount
                    # Inserting new object into the accumulation object
                    loansObj[loanId] = loanObj
            # Dumping to JSON the accumulation object
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(loansObj))
            
    class Users(webapp.RequestHandler):
        def get(self):
            usersObj = {}
            for bid in Bid.all():
                user = bid.user
                userId = user.key().id_or_name()
                if (userId not in usersObj):
                    userObj = {}
                    # Extracting properties
                    fundsAvailable = user.fundsAvailable
                    # Passing properties to the obj
                    userObj['userId'] = userId
                    userObj['fundsAvailable'] = fundsAvailable
                    # Inserting new object into the accumulation object
                    usersObj[userId] = userObj
            # Dumping to JSON the accumulation object
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(usersObj))
       
#################################################################

#TODO add groups grand to the urls
application = webapp.WSGIApplication(
                                     [('/mybids', MyBids),
                                      ('/bidWindow/bids', BidWindow.Bids),
                                      ('/bidWindow/loans', BidWindow.Loans),
                                      ('/bidWindow/users', BidWindow.Users),
                                      ('/bids', BidsRest),
                                      ('/users', UsersRest),
                                      ('/manusers', ManUsers),
                                      ('/home', Home),
                                      ('/logout', Logout),
                                      ('/search', Search),
                                      ('/calc', Calc),
                                      ('/download', Download),
                                      ('/jsonLoans', jsonLoans),
                                      ('/loansModel', loansModel.loansModelInstance),
                                      ('/TestUsers', user.UserInstance),
                                      ('/TestBids', bid.BidsInstance),
                                      ('/jsonDelete', loansModel.jsonDelete),
                                      ('/labels', Labels),
                                      ('/', Login)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
