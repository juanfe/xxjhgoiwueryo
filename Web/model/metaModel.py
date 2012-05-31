'''
Created on Feb 14, 2012

This is a meta-class in order to dynamically support the current JSON files
The definition is complete, but needs a parser using reflection to dynamically build the object and maintain it.

@author: Leonardo Zuniga S
'''
from google.appengine.ext import db
from google.appengine.ext import webapp

class metaModel(db.Model):
    className = db.StringProperty(required=True) # These two must be proper python identifiers and not be in
    propKey = db.StringProperty(required=True)   # http://code.google.com/appengine/docs/python/datastore/modelclass.html#Disallowed_Property_Names
    propName = db.StringProperty(required=True)  # this can be the same as the previous one, but is the one present at the JSON file
    propVerbose = db.StringProperty(required=True)
    propType = db.StringProperty(required=True,choices=set(["IntegerProperty","FloatProperty","BooleanProperty",
                                                                 "StringProperty","TextProperty","ByteStringProperty",
                                                                 "BlobProperty","DateProperty","TimeProperty","DateTimeProperty",
                                                                 "GeoPtProperty","PostalAddressProperty","PhoneNumberProperty",
                                                                 "EmailProperty","UserProperty","IMProperty","LinkProperty",
                                                                 "CategoryProperty","RatingProperty","ReferenceProperty",
                                                                 "SelfReferenceProperty","blobstore.BlobReferenceProperty",
                                                                 "ListProperty","StringListProperty"]))
    propRequired = db.BooleanProperty(required=True,default=False)
    propDefault = db.StringProperty()
    propChoices = db.StringListProperty()

# For the JSON file these are the instances:
class metaModelInstance(webapp.RequestHandler):
    def get(self):
        metaModel(className="jsonModel",propKey="customer_account_key",propName="customer_account_key",propVerbose="MO Name",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="collateral_key",propName="collateral_key",propVerbose="Loan Number",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="address",propName="address",propVerbose="Property address",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="advance_amt",propName="advance_amt",propVerbose="MO advance amount",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="amortization_term",propName="amortization_term",propVerbose="amortization term",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="anncap_init",propName="anncap_init",propVerbose="Initial Rate Adjustment Cap",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="appraiser_name",propName="appraiser_name",propVerbose="appraiser name",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="armindex",propName="armindex",propVerbose="ARM Index",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="armlcap",propName="armlcap",propVerbose="Lifetime Rate Adjustment Cap",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="armlfloor",propName="armlfloor",propVerbose="Lifetime Floor Rate",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="armmargin",propName="armmargin",propVerbose="ARM Margin",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="armoption",propName="armoption",propVerbose="is loan an Option ARM?",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="armpcap",propName="armpcap",propVerbose="Periodic Rate Adjustment Cap",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="armpfloor",propName="Armpfloor",propVerbose="Periodic Rate Cap",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="armteaser",propName="armteaser",propVerbose="ARM Teaser",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="bankruptcy_chapter",propName="bankruptcy_chapter",propVerbose="bankruptcy chapter",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="bankruptcy_discharge_date",propName="bankruptcy_discharge_date",propVerbose="bankruptcy discharge date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="borr_1_age",propName="borr_1_age",propVerbose="Primary borrower age",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="borr_1_employ_flag",propName="borr_1_employ_flag",propVerbose="Primary borrower employment flag",propType="BooleanProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="borr_1_first_name",propName="borr_1_first_name",propVerbose="First Name (Primary Borrower)",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="borr_1_gender",propName="borr_1_gender",propVerbose="Primary borrower Gender",propType="StringProperty",propRequired=True,propChoices=["M","F"]).put()
        metaModel(className="jsonModel",propKey="borr_1_last_name",propName="borr_1_last_name",propVerbose="Last Name (Primary Borrower)",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="borr_1_marital_status",propName="borr_1_marital_status",propVerbose="Primary borrower marital status",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="borr_2_age",propName="borr_2_age",propVerbose="Secondary borrower age",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="borr_2_employ_flag",propName="borr_2_employ_flag",propVerbose="Secondary Borrower employment flag",propType="BooleanProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="borr_2_first_name",propName="borr_2_first_name",propVerbose="First Name (Secondary Borrower)",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="borr_2_gender",propName="borr_2_gender",propVerbose="Secondary borrower gender",propType="StringProperty",propRequired=False,propChoices=["M","F"]).put()
        metaModel(className="jsonModel",propKey="borr_2_last_name",propName="borr_2_last_name",propVerbose="Last Name (Secondary Borrower)",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="borr_2_marital_status",propName="borr_2_marital_status",propVerbose="Secondary borrower marital status",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="citizenship_flag",propName="citizenship_flag",propVerbose="Citizen Y/N",propType="BooleanProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="city",propName="city",propVerbose="Property city",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="corelogic_collateral_risk_score",propName="CoreLogic Collateral Risk Score",propVerbose="CoreLogic Collateral Risk Score",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="corelogic_fraud_risk_score",propName="CoreLogic Fraud Risk Score",propVerbose="CoreLogic Fraud Risk Score",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="cur_note_rate",propName="Cur_note_rate",propVerbose="Current note rate",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="curr_upb",propName="curr_upb",propVerbose="Current Unpaid Balance",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="debt_service_ratio",propName="debt_service_ratio",propVerbose="debt service ratio",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="doc_level_code",propName="doc_level_code",propVerbose="Document Level Code",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="du_case_number",propName="du_case_number",propVerbose="du case number",propType="IntegerProperty",propRequired=True,propDefault="1000100100").put()
        metaModel(className="jsonModel",propKey="du_response",propName="du_response",propVerbose="du response",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="effective_date",propName="effective_date",propVerbose="Request Date",propType="DateProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="fha_case_number",propName="FHA_Case_Number",propVerbose="FHA Case Number",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="fico_score",propName="fico_score",propVerbose="fico score",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="first_adj_max_initial_rate",propName="1st_adj_max_initial_rate",propVerbose="1st adjustment maximum initial rate",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="first_adj_min_initial_rate",propName="1st_adj_min_initial_rate",propVerbose="1st adjustment minimum initial rate",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="first_delinquent_date",propName="first_delinquent_date",propVerbose="first delinquent date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="first_payment_change_date",propName="First_payment_change_date",propVerbose="First payment change date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="first_rate_adjust_period",propName="first_rate_adjust_period",propVerbose="first rate adjustment period",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="first_rate_change_date",propName="first_rate_change_date",propVerbose="first rate change date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="firstdue",propName="firstdue",propVerbose="first payment due date",propType="DateProperty",propRequired=True,propDefault="2/1/2012").put()
        metaModel(className="jsonModel",propKey="foreclosure_satisfied_date",propName="foreclosure_satisfied_date",propVerbose="foreclosure satisfied date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="funding_amount",propName="funding_amount",propVerbose="Amount Sent",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="funding_id",propName="funding_id",propVerbose="funding id",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="funding_method_code",propName="funding_method_code",propVerbose="funding method code",propType="IntegerProperty",propRequired=True,propDefault="1").put()
        metaModel(className="jsonModel",propKey="initial_recast_period",propName="Initial_recast_period",propVerbose="Initial recast period",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="interest_only_end_date",propName="Interest_Only_End_Date",propVerbose="Interest Only End Date",propType="DateProperty").put()
        metaModel(className="jsonModel",propKey="interest_only_flag",propName="interest_only_flag",propVerbose="interest only flag",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="interest_only_period",propName="interest_only_period",propVerbose="interest only  period",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="interest_rounding_feature",propName="Interest_rounding_feature",propVerbose="Interest rounding feature",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="interest_rounding_percentage",propName="Interest_rounding_percentage",propVerbose="Interest rounding percentage",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="inv_commit_date",propName="inv_commit_date",propVerbose="Investor Commitment Date",propType="DateProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="inv_commit_expire_date",propName="inv_commit_expire_date",propVerbose="Investor Commitment Expire Date",propType="DateProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="inv_commit_number",propName="inv_commit_number",propVerbose="Investor Commitment Number",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="inv_commit_price",propName="inv_commit_price",propVerbose="Investor Commitment Price",propType="IntegerProperty",propRequired=True,propDefault="100").put()
        metaModel(className="jsonModel",propKey="investor_code",propName="investor_code",propVerbose="investor code",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="investor_id",propName="investor_id",propVerbose="investor id",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="is_adjustable",propName="is_adjustable",propVerbose="is interest rate adjustable?",propType="BooleanProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="is_assets_verified",propName="is_assets_verified",propVerbose="Assets verified?",propType="BooleanProperty",propRequired=True,propDefault="True").put()
        metaModel(className="jsonModel",propKey="is_balloon",propName="Is_balloon",propVerbose="Is loan a balloon?",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="is_escrow_required",propName="is_escrow_required",propVerbose="is escrow required?",propType="BooleanProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="is_first_time_buyer",propName="is_first_time_buyer",propVerbose="is first time buyer?",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="is_lpmi",propName="Is_LPMI",propVerbose="Is LPMI",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="is_negam",propName="is_negam",propVerbose="is loan negatively amortizing?",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="junior_lien_amount",propName="Junior_lien_amount",propVerbose="Junior lien amount",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="lien_position",propName="lien_position",propVerbose="lien position",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="loan_officer",propName="Loan Officer",propVerbose="Loan Officer",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="loan_type",propName="Loan_Type",propVerbose="Loan Type",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="look_back_period",propName="Look_back_period",propVerbose="Look back period",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="lpmi_pct",propName="LPMI_PCT",propVerbose="LPMI Percentage",propType="FloatProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="market_value_cap",propName="Market_value_cap",propVerbose="Market value cap",propType="IntegerProperty",propRequired=True,propDefault="100").put()
        metaModel(className="jsonModel",propKey="maturity",propName="maturity",propVerbose="maturity date",propType="DateProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="max_negam",propName="max_negam",propVerbose="maximum negatively amortization",propType="FloatProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="max_rate",propName="Max_Rate",propVerbose="Max Rate",propType="FloatProperty").put()
        metaModel(className="jsonModel",propKey="mers_min",propName="mers_min",propVerbose="mers min number",propType="StringProperty",propRequired=True,propDefault="100000000000000000").put()
        metaModel(className="jsonModel",propKey="mo_city",propName="MO City",propVerbose="MO City",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="mo_state",propName="MO State",propVerbose="MO State",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="mo_zip",propName="MO Zip",propVerbose="MO Zip",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="mtg_ins_company",propName="mtg_ins_company",propVerbose="mortgage insurance company",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="mtg_ins_pct",propName="mtg_ins_pct",propVerbose="Mortgage Insurance",propType="BooleanProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="nmls_n",propName="NMLS #",propVerbose="NMLS #",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="occupancy_code",propName="occupancy_code",propVerbose="occupancy code",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="orig_appraised_value",propName="orig_appraised_value",propVerbose="original appraised value",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="orig_p_i",propName="orig_p_i",propVerbose="Original Principal & Interest Payment",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="orig_rate",propName="orig_rate",propVerbose="Original Interest Rate",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="orig_upb",propName="orig_upb",propVerbose="Original Unpaid Balance",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="original_cltv",propName="original_cltv",propVerbose="original cltv",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="original_ltv",propName="original_ltv",propVerbose="original ltv",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="original_term",propName="original_term",propVerbose="original term",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="origination_date",propName="origination_date",propVerbose="origination date",propType="DateProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="paid_to_date",propName="paid_to_date",propVerbose="paid to date",propType="DateProperty",propRequired=True,propDefault="1/1/2012").put()
        metaModel(className="jsonModel",propKey="payee1_abanum",propName="payee1_abanum",propVerbose="1st payee ABA number",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee1_accountnum",propName="payee1_accountnum",propVerbose="1st payee account number",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee1_address",propName="payee1_address",propVerbose="1st Payee Address",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee1_city",propName="payee1_city",propVerbose="1st Payee City",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="payee1_instruction1",propName="payee1_instruction1",propVerbose="1st Payee Wire Instruction 1",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee1_instruction2",propName="payee1_instruction2",propVerbose="1st Payee Wire Instruction 2",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee1_name",propName="payee1_name",propVerbose="1st Payee Name",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="payee1_state",propName="payee1_state",propVerbose="1st Payee State",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="payee1_zip",propName="payee1_zip",propVerbose="1st Payee Zip",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="payee2_abanum",propName="payee2_abanum",propVerbose="2nd payee ABA number",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_accountnum",propName="payee2_accountnum",propVerbose="2nd payee account number",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_address",propName="payee2_address",propVerbose="2nd Payee Address",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_city",propName="payee2_city",propVerbose="2nd Payee City",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_instruction1",propName="payee2_instruction1",propVerbose="2nd Payee Wire Instruction 1",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_instruction2",propName="payee2_instruction2",propVerbose="2nd Payee Wire Instruction 2",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_name",propName="payee2_name",propVerbose="2nd Payee Name",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_state",propName="payee2_state",propVerbose="2nd Payee State",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="payee2_zip",propName="payee2_zip",propVerbose="2nd Payee Zip",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="prepay_enforceability",propName="prepay_enforceability",propVerbose="prepay enforceability",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="prepay_penalty_flag",propName="prepay_penalty_flag",propVerbose="prepayment penalty flag",propType="BooleanProperty",propRequired=True,propDefault="False").put()
        metaModel(className="jsonModel",propKey="prepay_penalty_pct",propName="prepay_penalty_pct",propVerbose="prepayment penalty percentage",propType="FloatProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="prepay_period",propName="prepay_period",propVerbose="prepayment period",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="product_code",propName="product_code",propVerbose="Loan Type",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="property_type_code",propName="property_type_code",propVerbose="property type code",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="purchase_price",propName="purchase_price",propVerbose="purchase price",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="purpose_code",propName="purpose_code",propVerbose="purpose code",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="rate_change_frequency",propName="rate_change_frequency",propVerbose="rate adjustment frequency",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="reserved_amt",propName="reserved_amt",propVerbose="reserved amount",propType="FloatProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="reserved_term",propName="reserved_term",propVerbose="reserved term",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="servicer",propName="Servicer",propVerbose="Servicer",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="servicing_fee",propName="Servicing_fee",propVerbose="Servicing fee",propType="FloatProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="ss_number",propName="ss_number",propVerbose="SS# (Primary Borrower)",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="ss_number_2",propName="ss_number_2",propVerbose="SS# (Secondary Borrower)",propType="StringProperty").put()
        metaModel(className="jsonModel",propKey="state",propName="state",propVerbose="Property state",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="subsequent_recast_period",propName="subsequent_recast_period",propVerbose="subsequent recast period",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="teaser_period",propName="teaser_period",propVerbose="teaser period",propType="IntegerProperty").put()
        metaModel(className="jsonModel",propKey="times_delinquent_120",propName="times_delinquent_120",propVerbose="times delinquent 120",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="times_delinquent_30",propName="times_delinquent_30",propVerbose="times delinquent 30",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="times_delinquent_60",propName="times_delinquent_60",propVerbose="times delinquent 60",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="times_delinquent_90",propName="times_delinquent_90",propVerbose="times delinquent 90",propType="IntegerProperty",propRequired=True,propDefault="0").put()
        metaModel(className="jsonModel",propKey="tradelines",propName="tradelines",propVerbose="tradelines",propType="IntegerProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="u_w",propName="U/W",propVerbose="Loan Underwriter",propType="StringProperty",propRequired=True).put()
        metaModel(className="jsonModel",propKey="units",propName="units",propVerbose="units",propType="IntegerProperty",propRequired=True,propDefault="1").put()
        metaModel(className="jsonModel",propKey="pzip",propName="zip",propVerbose="Property zip",propType="StringProperty",propRequired=True).put()