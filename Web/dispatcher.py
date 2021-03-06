import StringIO
import csv
import random
import logging
from google.appengine.api import users, memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson as json
from datetime import datetime, timedelta, date
from model import user, bid
from model.demo_loan import LoanInstance
from model.demo_bid import BidsInstance
from model.demo_user import UsrInstance
from model.bid import Bid
from model.user import User
from model.user import PageAllowed, getGroup, getCurrentUser, getPageDict, getTheUser
from model.page import Page
from model import loan
from calc import calc
from demo import Demo_Param_Calc
from lserrors import CalcError

#Rendering logic


class Home(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo']) #, 'Broker', 'MO', 'Engine'])
    def get(self):
        page = Page.HOME
        parameters = getPageDict(page)
        parameters['User'] = "%s %s" % (getCurrentUser(), getGroup())
        self.response.out.write(template.render("templates/home.html",
                parameters))


class Search(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker', 'MO', 'Engine', 'Demo'])
    def get(self):
        page = Page.SEARCH
        parameters = getPageDict(page)
        parameters['User'] = "%s %s" % (getCurrentUser(), getGroup())
        self.response.out.write(template.render("templates/search.html",
                parameters))


class Calc(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Engine', 'Demo'])
    def get(self):
        page = Page.CALC
        parameters = getPageDict(page)
        parameters['User'] = "%s %s" % (getCurrentUser(), getGroup())
        try:
            c = calc()
            logging.debug(80*"*")
            logging.debug("loans =")
            logging.debug(c['loans'])
            logging.debug(80*"*")
            logging.debug("bids =")
            logging.debug(c['bids'])
            if 'loans' in c and 'bids' in c:
                parameters['loans'] = c['loans']
                parameters['bids'] = c['bids']
            for i in range(1, len(c['bids'])):
                b = Bid.get_by_key_name(key_names = c['bids'][i][0]['bid'])
                for j in range(len(c['bids'][i])):
                    if 'key' in c['bids'][i][j]:
                        l = loan.getLoan(c['bids'][i][j]['key'])
                        if (l.curr_upb >= long(float(c['bids'][i][j]['val']))):
                            l.curr_upb -= long(float(c['bids'][i][j]['val']))
                            l.put()
                        else:
                            raise CalcError("ERROR: At discount Bit %s to Loan %s curr_upb %s" %
                                    (str(c['bids'][i][0]['bid']), str(l.collateral_key),
                                    str(l.curr_upb)))
   
                b.status = 'Accepted'
                b.put()
            self.response.out.write(template.render("templates/results.html",
                    parameters))
        except:
            g = getGroup()
            if g == 'Demo':
                c = Demo_Param_Calc()
                parameters['loans'] = c['loans']
                parameters['bids'] = c['bids']
                self.response.out.write(template.render(
                        "templates/results.html", parameters))
            else:
                self.response.out.write(template.render("templates/oops.html",
                        []))


class MyBids(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker', 'MO', 'Engine', 'Demo'])
    def get(self):
        page = Page.MYBIDS
        parameters = getPageDict(page)
        parameters['User'] = "%s %s" % (getCurrentUser(), getGroup())
        self.response.out.write(template.render("templates/mybids.html",
                parameters))


class ManUsers(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker', 'Demo'])
    def get(self):
        page = Page.USERS
        parameters = getPageDict(page)
        parameters['User'] = "%s %s" % (getCurrentUser(), getGroup())
        self.response.out.write(template.render("templates/users.html",
                parameters))


#Storage of the dojo bids json
dojoAjaxKey = 'bids'


# TODO add decorator
class BidsRest(webapp.RequestHandler):
    def post(self):
        bidsToAddJson = self.request.get(dojoAjaxKey)
        bidsToAddObj = json.loads(bidsToAddJson)
        # Adding the bid model objects
        dbUser = getTheUser(users.get_current_user())
        # Getting the bids for the current user
        userBids = dbUser.bids
        currentBids = {}
        #TODO if the user is an admin, then add all the bids
        #TODO if the user is a MO, the add the users for the MO
        i = 0 
        for bid in userBids:
            if bid.loan:
                currentBids[bid.loan.collateral_key] = bid
            else:
                currentBids[i] = bid
                i += 1
               
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
                loanQuery = loan.Loan.all(). \
                        filter('collateral_key =', key)
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
                        ordertype = 'Noncompetitive' if bidrate else
                                'Competitive',
                        status = status,
                        createdAt = creationTime,
                        expiresAt = expirationTime,
                        #Added to agree with the LiqSpop engine
                        #TODO is better to put it on the web
                        bidtype = 'Specified',
                        lorm = 'Loan',
                        ordertiming = 'Day Trade',
                        key_name = "%s %s" % (getCurrentUser(),
                            creationTime),
                    ).put()

    def get(self):
        # Getting bids from the Db
        bidsModelObj = []
        modelBids = getTheUser(users.get_current_user()).bids
        #TODO add the new fields
        for modelBid in modelBids:
            bidModelObj = {}
            if modelBid.loan:
                bidModelObj['collateral_key'] = modelBid.loan.collateral_key
            else:
                bidModelObj['collateral_key'] = ""
            bidModelObj['participation'] = modelBid.participation
            bidModelObj['bidrate'] = modelBid.bidrate
            bidModelObj['status'] = modelBid.status
            bidModelObj['createdAt'] = modelBid.createdAt. \
                    strftime('%Y/%m/%d %H:%M:%S')
            bidModelObj['expiresAt'] = modelBid.expiresAt. \
                    strftime('%Y/%m/%d %H:%M:%S')
            bidsModelObj.append(bidModelObj)
        # Wrapping and sending
        itemsWrapper = {}
        itemsWrapper['items'] = bidsModelObj
        bidsToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(bidsToSendJson)

    def delete(self):
        bidsToDeleteJson = self.request.get(dojoAjaxKey)
        bidsToDeleteObj = json.loads(bidsToDeleteJson)
        userBids = getTheUser(users.get_current_user()).bids
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
    #    usersToAddJson = self.request.get(dojoAjaxKey)
    #    usersToAddObj =  json.loads(usersToAddJson)
    #    # Adding the bid model objects
    #    ##dbUser = getTheUser(users.get_current_user())
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
    #            loanQuery = loan.Loan.all().
    #                    filter('collateral_key =', key)
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
    #                      ordertype = 'Competitive' if bidrate !=
    #                               None else 'Noncompetitive',
    #                      status = status,
    #                      createdAt = creationTime,
    #                      expiresAt = expirationTime,
    #                      #Added to agree with the LiqSpop engine
    #                      #TODO is better to put it on the web
    #                      bidtype = 'Specified',
    #                      lorm = 'Loan',
    #                      ordertiming = 'Day Trade',
    #                      key_name = "%s %s"%(getCurrentUser(),
    #                              creationTime),
    #                      ).put()

    def get(self):
        # Getting Users from the Db
        usersModelObj = []
        modelUsers = User.all()
        for modelUser in modelUsers:
            userModelObj = {}
            userModelObj['account'] = str(modelUser.account)
            userModelObj['fundsAvailable'] = modelUser.fundsAvailable if \
                    modelUser.group == 'Broker' else '*****'
            userModelObj['group'] = modelUser.group
            usersModelObj.append(userModelObj)
        # Wrapping and sending
        itemsWrapper = {}
        itemsWrapper['items'] = usersModelObj
        usersToSendJson = json.dumps(itemsWrapper)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(usersToSendJson)

    #def delete(self):
    #    bidsToDeleteJson = self.request.get(dojoAjaxKey)
    #    bidsToDeleteObj =  json.loads(bidsToDeleteJson)
    #    userBids = getTheUser(users.get_current_user()).bids
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
        loans = loan.Loan.all()
        for _loan in loans:
            loanObj = {}
            for k, v in vars(_loan).items():
                k = k[1:]
                if k != 'entity' and k != 'from_entity':
                    if type(v) == type(datetypeObj):
                        loanObj[k] = '{0}/{1}/{2}'.format(v.month, v.day,
                                v.year)
                            # strftime('%m/%d/%Y')
                    elif type(v) == bool:
                        loanObj[k] = 1 if v else 0
                    elif type(v) == type(nonetypeObj):
                        loanObj[k] = ''
                    else:
                        loanObj[k] = v
#                    self.response.out.write('{0}({1}) {2}\n'.
#                            format(k,type(loanObj[k]),loanObj[k]))
#            self.response.out.write('\n\n')
            loanJsonObj.append(loanObj)
        itemsWrapper = {}
        itemsWrapper['items'] = loanJsonObj
        return json.dumps(itemsWrapper)


class Login(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Broker', 'MO', 'Engine', 'Demo'])
    def get(self):
        self.redirect('/home')


class UserInstance(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo'])
    def get(self):
        UsrInstance().get()
        UsrInstance().get_demo()
        self.redirect('/home')


class TestingInstance(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo'])
    def get(self):
        LoanInstance().get()
        BidsInstance().get()
        self.redirect('/home')


class UpdateDemoData(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo'])
    def get(self):
        UsrInstance().UpdateDemoData()
        BidsInstance().UpdateDemoData()
        LoanInstance().UpdateDemoData()
        self.redirect('/home')


class TestingLoans(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo'])
    def get(self):
        LoanInstance().get()
        self.redirect('/home')
        

class TestingBids(webapp.RequestHandler):
    @PageAllowed(['Admin', 'Demo'])
    def get(self):
        BidsInstance().get()
        self.redirect('/home')


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
        self.response.headers['Content-Disposition'] = \
                'attachment;filename=\"Loans Details.csv\"'
        bidsJson = self.request.get(dojoAjaxKey)
        bidsCsv = jsonToCsv(bidsJson)
        self.response.out.write(bidsCsv)


class Labels(webapp.RequestHandler):
    def get(self):
        fieldToLabelDict = {}
        # models where the labels are defined as verbose names
        models = [loan.Loan, Bid]
        for model in models:
            fieldToLabelDict.update(
                    self.getModelPropertiesFieldToVerboseNameDict(model))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(fieldToLabelDict))

    def getModelPropertiesFieldToVerboseNameDict(self, model):
        propertiesFieldToVerboseNamesDict = {}
        for field, modelProperty in model.properties().iteritems():
            propertiesFieldToVerboseNamesDict[field] = \
                    modelProperty.verbose_name
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
                if bidRate > 0:
                    orderType = 'Competitive'
                else:
                    orderType = 'Noncompetitive'
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
                                      ('/UserTesting', UserInstance),
                                      ('/DataTesting', TestingInstance),
                                      ('/RecreateData', UpdateDemoData),
                                      ('/LoanTesting', TestingLoans),
                                      ('/BidTesting', TestingBids),
                                      ('/labels', Labels),
                                      ('/', Login)
                                     ],
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
