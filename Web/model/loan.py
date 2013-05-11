"""
Created on Feb 14, 2012

@author: Leonardo Zuniga S
         Juan Fernando Jaramillo Botero
"""
from google.appengine.ext import db, webapp
from datetime import datetime
from user import PageAllowed


# This is an extensible class with all the parameter definitions present in the JSON files
class Loan(db.Model):
    customer_account_key = db.StringProperty(verbose_name="MO Name")
    collateral_key = db.StringProperty(verbose_name="Loan Number")
    address = db.StringProperty(verbose_name="Property address")
    advance_amt = db.IntegerProperty(verbose_name="MO advance amount")
    amortization_term = db.IntegerProperty(verbose_name="amortization term")
    anncap_init = db.IntegerProperty(verbose_name="Initial Rate Adjustment Cap")
    appraiser_name = db.StringProperty(verbose_name="appraiser name")
    armindex = db.StringProperty(verbose_name="ARM Index")
    armlcap = db.IntegerProperty(verbose_name="Lifetime Rate Adjustment Cap")
    armlfloor = db.FloatProperty(verbose_name="Lifetime Floor Rate")
    armmargin = db.FloatProperty(verbose_name="ARM Margin")
    armoption = db.BooleanProperty(verbose_name="is loan an Option ARM?",default=False)
    armpcap = db.IntegerProperty(verbose_name="Periodic Rate Adjustment Cap")
    armpfloor = db.IntegerProperty(verbose_name="Periodic Rate Cap")
    armteaser = db.FloatProperty(verbose_name="ARM Teaser")
    bankruptcy_chapter = db.StringProperty(verbose_name="bankruptcy chapter")
    bankruptcy_discharge_date = db.DateProperty(verbose_name="bankruptcy discharge date")
    borr_1_age = db.IntegerProperty(verbose_name="Primary borrower age")
    borr_1_employ_flag = db.BooleanProperty(verbose_name="Primary borrower employment flag")
    borr_1_first_name = db.StringProperty(verbose_name="First Name (Primary Borrower)")
    borr_1_gender = db.StringProperty(verbose_name="Primary borrower Gender",choices=set(["M","F"]))
    borr_1_last_name = db.StringProperty(verbose_name="Last Name (Primary Borrower)")
    borr_1_marital_status = db.StringProperty(verbose_name="Primary borrower marital status")
    borr_2_age = db.IntegerProperty(verbose_name="Secondary borrower age")
    borr_2_employ_flag = db.BooleanProperty(verbose_name="Secondary Borrower employment flag")
    borr_2_first_name = db.StringProperty(verbose_name="First Name (Secondary Borrower)")
    borr_2_gender = db.StringProperty(verbose_name="Secondary borrower gender",choices=set(["M","F"]))
    borr_2_last_name = db.StringProperty(verbose_name="Last Name (Secondary Borrower)")
    borr_2_marital_status = db.StringProperty(verbose_name="Secondary borrower marital status")
    citizenship_flag = db.BooleanProperty(verbose_name="Citizen Y/N")
    city = db.StringProperty(verbose_name="Property city")
    corelogic_collateral_risk_score = db.IntegerProperty(verbose_name="CoreLogic Collateral Risk Score")
    corelogic_fraud_risk_score = db.IntegerProperty(verbose_name="CoreLogic Fraud Risk Score")
    cur_note_rate = db.FloatProperty(verbose_name="Current note rate")
    curr_upb = db.IntegerProperty(verbose_name="Current Unpaid Balance")
    debt_service_ratio = db.FloatProperty(verbose_name="debt service ratio")
    doc_level_code = db.IntegerProperty(verbose_name="Document Level Code")
    du_case_number = db.IntegerProperty(verbose_name="du case number",default="1000100100")
    du_response = db.StringProperty(verbose_name="du response")
    effective_date = db.DateProperty(verbose_name="Request Date")
    fha_case_number = db.StringProperty(verbose_name="FHA Case Number")
    fico_score = db.IntegerProperty(verbose_name="fico score")
    first_adj_max_initial_rate = db.FloatProperty(verbose_name="1st adjustment maximum initial rate")
    first_adj_min_initial_rate = db.FloatProperty(verbose_name="1st adjustment minimum initial rate")
    first_delinquent_date = db.DateProperty(verbose_name="first delinquent date")
    first_payment_change_date = db.DateProperty(verbose_name="First payment change date")
    first_rate_adjust_period = db.IntegerProperty(verbose_name="first rate adjustment period")
    first_rate_change_date = db.DateProperty(verbose_name="first rate change date")
    firstdue = db.DateProperty(verbose_name="first payment due date",default=datetime.strptime("2/1/2012","%m/%d/%Y").date())
    foreclosure_satisfied_date = db.DateProperty(verbose_name="foreclosure satisfied date")
    funding_amount = db.FloatProperty(verbose_name="Amount Sent")
    funding_id = db.IntegerProperty(verbose_name="funding id")
    funding_method_code = db.IntegerProperty(verbose_name="funding method code",default=1)
    initial_recast_period = db.IntegerProperty(verbose_name="Initial recast period")
    interest_only_end_date = db.DateProperty(verbose_name="Interest Only End Date")
    interest_only_flag = db.BooleanProperty(verbose_name="interest only flag",default=False)
    interest_only_period = db.IntegerProperty(verbose_name="interest only  period",default=0)
    interest_rounding_feature = db.StringProperty(verbose_name="Interest rounding feature")
    interest_rounding_percentage = db.FloatProperty(verbose_name="Interest rounding percentage")
    inv_commit_date = db.DateProperty(verbose_name="Investor Commitment Date")
    inv_commit_expire_date = db.DateProperty(verbose_name="Investor Commitment Expire Date")
    inv_commit_number = db.IntegerProperty(verbose_name="Investor Commitment Number")
    inv_commit_price = db.IntegerProperty(verbose_name="Investor Commitment Price",default=100)
    investor_code = db.StringProperty(verbose_name="investor code")
    investor_id = db.StringProperty(verbose_name="investor id")
    is_adjustable = db.BooleanProperty(verbose_name="is interest rate adjustable?")
    is_assets_verified = db.BooleanProperty(verbose_name="Assets verified?",default=True)
    is_balloon = db.BooleanProperty(verbose_name="Is loan a balloon?",default=False)
    is_escrow_required = db.BooleanProperty(verbose_name="is escrow required?")
    is_first_time_buyer = db.BooleanProperty(verbose_name="is first time buyer?",default=False)
    is_lpmi = db.BooleanProperty(verbose_name="Is LPMI",default=False)
    is_negam = db.BooleanProperty(verbose_name="is loan negatively amortizing?",default=False)
    junior_lien_amount = db.IntegerProperty(verbose_name="Junior lien amount",default=0)
    lien_position = db.IntegerProperty(verbose_name="lien position")
    loan_officer = db.StringProperty(verbose_name="Loan Officer")
    loan_type = db.StringProperty(verbose_name="Loan Type")
    look_back_period = db.IntegerProperty(verbose_name="Look back period")
    lpmi_pct = db.FloatProperty(verbose_name="LPMI Percentage",default=0.0)
    market_value_cap = db.IntegerProperty(verbose_name="Market value cap",default=100)
    maturity = db.DateProperty(verbose_name="maturity date")
    max_negam = db.FloatProperty(verbose_name="maximum negatively amortization",default=0)
    max_rate = db.FloatProperty(verbose_name="Max Rate")
    mers_min = db.StringProperty(verbose_name="mers min number",default="100000000000000000")
    mo_city = db.StringProperty(verbose_name="MO City")
    mo_state = db.StringProperty(verbose_name="MO State")
    mo_zip = db.StringProperty(verbose_name="MO Zip")
    mtg_ins_company = db.StringProperty(verbose_name="mortgage insurance company")
    mtg_ins_pct = db.BooleanProperty(verbose_name="Mortgage Insurance",default=False)
    nmls_n = db.IntegerProperty(verbose_name="NMLS #")
    occupancy_code = db.StringProperty(verbose_name="occupancy code")
    orig_appraised_value = db.IntegerProperty(verbose_name="original appraised value")
    orig_p_i = db.FloatProperty(verbose_name="Original Principal & Interest Payment")
    orig_rate = db.FloatProperty(verbose_name="Original Interest Rate")
    orig_upb = db.IntegerProperty(verbose_name="Original Unpaid Balance")
    original_cltv = db.FloatProperty(verbose_name="original cltv")
    original_ltv = db.FloatProperty(verbose_name="original ltv")
    original_term = db.IntegerProperty(verbose_name="original term")
    origination_date = db.DateProperty(verbose_name="origination date")
    paid_to_date = db.DateProperty(verbose_name="paid to date",default=datetime.strptime("1/1/2012","%m/%d/%Y").date())
    payee1_abanum = db.StringProperty(verbose_name="1st payee ABA number")
    payee1_accountnum = db.StringProperty(verbose_name="1st payee account number")
    payee1_address = db.StringProperty(verbose_name="1st Payee Address")
    payee1_city = db.StringProperty(verbose_name="1st Payee City")
    payee1_instruction1 = db.StringProperty(verbose_name="1st Payee Wire Instruction 1")
    payee1_instruction2 = db.StringProperty(verbose_name="1st Payee Wire Instruction 2")
    payee1_name = db.StringProperty(verbose_name="1st Payee Name")
    payee1_state = db.StringProperty(verbose_name="1st Payee State")
    payee1_zip = db.StringProperty(verbose_name="1st Payee Zip")
    payee2_abanum = db.StringProperty(verbose_name="2nd payee ABA number")
    payee2_accountnum = db.StringProperty(verbose_name="2nd payee account number")
    payee2_address = db.StringProperty(verbose_name="2nd Payee Address")
    payee2_city = db.StringProperty(verbose_name="2nd Payee City")
    payee2_instruction1 = db.StringProperty(verbose_name="2nd Payee Wire Instruction 1")
    payee2_instruction2 = db.StringProperty(verbose_name="2nd Payee Wire Instruction 2")
    payee2_name = db.StringProperty(verbose_name="2nd Payee Name")
    payee2_state = db.StringProperty(verbose_name="2nd Payee State")
    payee2_zip = db.StringProperty(verbose_name="2nd Payee Zip")
    prepay_enforceability = db.StringProperty(verbose_name="prepay enforceability")
    prepay_penalty_flag = db.BooleanProperty(verbose_name="prepayment penalty flag",default=False)
    prepay_penalty_pct = db.FloatProperty(verbose_name="prepayment penalty percentage",default=0.0)
    prepay_period = db.StringProperty(verbose_name="prepayment period")
    product_code = db.StringProperty(verbose_name="Loan Type")
    property_type_code = db.StringProperty(verbose_name="property type code")
    purchase_price = db.IntegerProperty(verbose_name="purchase price")
    purpose_code = db.StringProperty(verbose_name="purpose code")
    pzip = db.StringProperty(verbose_name="Property zip")
    rate_change_frequency = db.IntegerProperty(verbose_name="rate adjustment frequency")
    reserved_amt = db.FloatProperty(verbose_name="reserved amount")
    reserved_term = db.IntegerProperty(verbose_name="reserved term")
    servicer = db.StringProperty(verbose_name="Servicer")
    servicing_fee = db.FloatProperty(verbose_name="Servicing fee",default=0.0)
    ss_number = db.StringProperty(verbose_name="SS# (Primary Borrower)")
    ss_number_2 = db.StringProperty(verbose_name="SS# (Secondary Borrower)")
    state = db.StringProperty(verbose_name="Property state")
    subsequent_recast_period = db.IntegerProperty(verbose_name="subsequent recast period")
    teaser_period = db.IntegerProperty(verbose_name="teaser period")
    times_delinquent_30 = db.IntegerProperty(verbose_name="times delinquent 30",default=0)
    times_delinquent_60 = db.IntegerProperty(verbose_name="times delinquent 60",default=0)
    times_delinquent_90 = db.IntegerProperty(verbose_name="times delinquent 90",default=0)
    times_delinquent_120 = db.IntegerProperty(verbose_name="times delinquent 120",default=0)
    tradelines = db.IntegerProperty(verbose_name="tradelines")
    u_w = db.StringProperty(verbose_name="Loan Underwriter")
    units = db.IntegerProperty(verbose_name="units",default=1)

def getLoan(key):
    return db.get(db.Key.from_path("Loan", key))
