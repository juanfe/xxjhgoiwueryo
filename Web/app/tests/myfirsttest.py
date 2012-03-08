'''
Created on Mar 8, 2012

@author: Camilo
'''

import unittest, random, time, json
from datetime import datetime, timedelta
from webtest import TestApp

from google.appengine.ext import db, testbed
from google.appengine.api import users

from dispatcher import application
from model.loansModel import loansModel
from ls.model.user import User
from ls.model.bid import Bid

class MyFirstTest(unittest.TestCase):

    def setUp(self):

        self.testbed = testbed.Testbed()

        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.setup_env(app_id='liquidityspot')
        self.testbed.activate()

        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()

        # create a test server for us to prod
        self.testapp = TestApp(application)

    def tearDown(self):            
        self.testbed.deactivate()

    def testEmptyObjWithNoBids(self):
        result = self.testapp.get("/bidWindow/bids")
        self.assertEqual(result.body, "{}")
    
    def testEmptyObjWithNoLoans(self):
        result = self.testapp.get("/bidWindow/loans")
        self.assertEqual(result.body, "{}")
        
    def testEmptyObjWithNoUsers(self):
        result = self.testapp.get("/bidWindow/users")
        self.assertEqual(result.body, "{}")
        
    def testSingleBid(self):
        # Creating a loan
        loan = loansModel(key_name="201149912",customer_account_key="ABCD",collateral_key="201149912",advance_amt=176021,amortization_term=120,appraiser_name="ABC APPRAISAL",armmargin=0.0,armoption=False,borr_1_age=43,borr_1_employ_flag=False,borr_1_gender="M",borr_1_last_name="Bushey",borr_1_marital_status="Single",citizenship_flag=True,city="Brush Prairie",cur_note_rate=4.3750,curr_upb=232000,debt_service_ratio=20.8011040,doc_level_code=3,du_case_number=1000100100,du_response="Approve/Eligible",effective_date=datetime.strptime("12/16/2011","%m/%d/%Y").date(),corelogic_collateral_risk_score=323,corelogic_fraud_risk_score=783,fico_score=741,firstdue=datetime.strptime("2/1/2012","%m/%d/%Y").date(),funding_method_code=1,interest_only_flag=False,interest_only_period=0,inv_commit_date=datetime.strptime("12/17/2011","%m/%d/%Y").date(),inv_commit_expire_date=datetime.strptime("1/16/2012","%m/%d/%Y").date(),inv_commit_number=1111111,inv_commit_price=100,investor_code="JPM",is_adjustable=False,is_assets_verified=True,is_balloon=False,is_escrow_required=True,is_first_time_buyer=False,is_lpmi=False,is_negam=False,junior_lien_amount=0,lien_position=1,loan_officer="Lane",loan_type="Conv No PMI",lpmi_pct=0.0,market_value_cap=100,maturity=datetime.strptime("2/1/2022","%m/%d/%Y").date(),max_negam=0.0,mers_min="100000000000000000",mo_city="Brush Prairie",mtg_ins_pct=False,nmls_n=1234,occupancy_code="O",orig_appraised_value=232000,orig_p_i=1160.0,orig_rate=4.3750,orig_upb=232000,original_cltv=35.8310,original_ltv=35.8310,original_term=120,origination_date=datetime.strptime("12/16/2011","%m/%d/%Y").date(),paid_to_date=datetime.strptime("1/1/2012","%m/%d/%Y").date(),payee1_city="Brush Prairie",payee1_name="Title Company ABC",payee1_state="WA",payee1_zip="98606",prepay_penalty_flag=False,prepay_penalty_pct=0.0,product_code="CONF10F",property_type_code="SFR",purchase_price=232000,purpose_code="CO",reserved_amt=20808.220,reserved_term=15,servicing_fee=0.0,ss_number="000000002",state="WA",times_delinquent_30=0,times_delinquent_60=0,times_delinquent_90=0,times_delinquent_120=0,tradelines=2,u_w="Charles",units=1,zip="98606",anncap_init=0,armlcap=0,armlfloor=0.00,armpcap=0,armpfloor=0,borr_2_age=0,borr_2_employ_flag=False,initial_recast_period=0,max_rate=4.3750,mo_state="WA",mo_zip="98606",rate_change_frequency=0,subsequent_recast_period=0,teaser_period=0)
        loan.put()
        # Creating an user
        userEmail = "test@example.com"
        apiUser = users.User(userEmail)
        User.account.auto_current_user = False
        user = User(key_name = userEmail, account = apiUser)
        user.fundsAvailable = random.randint(100,1000) * 1000
        user.put()
        #Values for the bid
        participation = 10.0
        bidrate = 1.5
        creationTime = datetime.now()
        expirationTime = creationTime + timedelta(hours=2)
        status = random.choice(Bid.status.choices)
        #Creating a bid
        Bid(parent = user,
            user = user,
            loan = loan,
            participation = participation,
            bidrate = bidrate,
            status = status,
            createdAt = creationTime,
            expiresAt = expirationTime).put()
        #time.sleep(20)
        result = self.testapp.get("/bidWindow/bids")
        # Base json
        bid = Bid.all().get()
        bidsObj = {}
        bidObj = {}
        bidId = bid.key().id_or_name()
        bidObj['bidId'] = bidId
        bidObj['date'] = creationTime.strftime("%Y-%m-%d")
        bidObj['time'] = creationTime.strftime("%H:%M:%S")
        bidObj['bidType'] = 'Specified'
        bidObj['participation'] = participation
        bidObj['assetSubset'] = 'Loan'
        bidObj['loanId'] = loan.key().id_or_name()
        bidObj['orderType'] = 'Competitive'
        bidObj['bidRate'] = bidrate
        bidObj['orderTiming'] = 'Day Trade'
        bidObj['userId'] = user.key().id_or_name()
        bidsObj[bidId] = bidObj
        # comparing json
        jsonToCompare = json.dumps(bidsObj)
        
        self.assertEqual(result.body, jsonToCompare)
        
        