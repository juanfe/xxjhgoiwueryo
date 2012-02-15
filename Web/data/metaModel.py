'''
Created on Feb 14, 2012

This is a meta-class in order to dynamically support the current JSON files
The definition is complete, but needs a parser using reflection to dynamically build the object and maintain it.

@author: Leonardo Zuniga S
'''
from google.appengine.ext import db

class metaModel(db.Model):
    className = db.StringProperty(required=True) # These two must be proper python identifiers and not be in
    propKey = db.StringProperty(required=True)   # http://code.google.com/appengine/docs/python/datastore/modelclass.html#Disallowed_Property_Names
    propName = db.StringProperty(required=True)  # this can be the same as the previous one, but is the one present at the JSON file
    propVerbose = db.StringProperty(required=True)
    propType = db.StringProperty(required=True, choices=set(["IntegerProperty","FloatProperty","BooleanProperty",
                                                                 "StringProperty","TextProperty","ByteStringProperty",
                                                                 "BlobProperty","DateProperty","TimeProperty","DateTimeProperty",
                                                                 "GeoPtProperty","PostalAddressProperty","PhoneNumberProperty",
                                                                 "EmailProperty","UserProperty","IMProperty","LinkProperty",
                                                                 "CategoryProperty","RatingProperty","ReferenceProperty",
                                                                 "SelfReferenceProperty","blobstore.BlobReferenceProperty",
                                                                 "ListProperty","StringListProperty"]))
    propRequired = db.BooleanProperty(required=True, default=False)
    propDefault = db.StringProperty()
    propChoices = db.StringListProperty()

# For the JSON file these are the instances:
metaModel("jsonModel","customer_account_key","customer_account_key","MO Name","StringProperty",True).put()
metaModel("jsonModel","collateral_key","collateral_key","Loan Number","IntegerProperty",True).put()
metaModel("jsonModel","address","address","Property address","StringProperty").put()
metaModel("jsonModel","advance_amt","advance_amt","MO advance amount","IntegerProperty",True).put()
metaModel("jsonModel","amortization_term","amortization_term","amortization term","IntegerProperty",True).put()
metaModel("jsonModel","anncap_init","anncap_init","Initial Rate Adjustment Cap","IntegerProperty").put()
metaModel("jsonModel","appraiser_name","appraiser_name","appraiser name","StringProperty",True).put()
metaModel("jsonModel","armindex","armindex","ARM Index","StringProperty").put()
metaModel("jsonModel","armlcap","armlcap","Lifetime Rate Adjustment Cap","IntegerProperty").put()
metaModel("jsonModel","armlfloor","armlfloor","Lifetime Floor Rate","FloatProperty").put()
metaModel("jsonModel","armmargin","armmargin","ARM Margin","IntegerProperty",True).put()
metaModel("jsonModel","armoption","armoption","is loan an Option ARM?","BooleanProperty",True,False).put()
metaModel("jsonModel","armpcap","armpcap","Periodic Rate Adjustment Cap","IntegerProperty").put()
metaModel("jsonModel","armpfloor","Armpfloor","Periodic Rate Cap","IntegerProperty").put()
metaModel("jsonModel","armteaser","armteaser","ARM Teaser","FloatProperty").put()
metaModel("jsonModel","bankruptcy_chapter","bankruptcy_chapter","bankruptcy chapter","StringProperty").put()
metaModel("jsonModel","bankruptcy_discharge_date","bankruptcy_discharge_date","bankruptcy discharge date","DateProperty").put()
metaModel("jsonModel","borr_1_age","borr_1_age","Primary borrower age","IntegerProperty",True).put()
metaModel("jsonModel","borr_1_employ_flag","borr_1_employ_flag","Primary borrower employment flag","BooleanProperty",True).put()
metaModel("jsonModel","borr_1_first_name","borr_1_first_name","First Name (Primary Borrower)","StringProperty").put()
metaModel("jsonModel","borr_1_gender","borr_1_gender","Primary borrower Gender","StringProperty",True, None, ["M","F"]).put()
metaModel("jsonModel","borr_1_last_name","borr_1_last_name","Last Name (Primary Borrower)","StringProperty",True).put()
metaModel("jsonModel","borr_1_marital_status","borr_1_marital_status","Primary borrower marital status","StringProperty",True).put()
metaModel("jsonModel","borr_2_age","borr_2_age","Secondary borrower age","IntegerProperty").put()
metaModel("jsonModel","borr_2_employ_flag","borr_2_employ_flag","Secondary Borrower employment flag","BooleanProperty",True).put()
metaModel("jsonModel","borr_2_first_name","borr_2_first_name","First Name (Secondary Borrower)","StringProperty").put()
metaModel("jsonModel","borr_2_gender","borr_2_gender","Secondary borrower gender","StringProperty",False, None, ["M","F"]).put()
metaModel("jsonModel","borr_2_last_name","borr_2_last_name","Last Name (Secondary Borrower)","StringProperty").put()
metaModel("jsonModel","borr_2_marital_status","borr_2_marital_status","Secondary borrower marital status","StringProperty").put()
metaModel("jsonModel","citizenship_flag","citizenship_flag","Citizen Y/N","BooleanProperty",True).put()
metaModel("jsonModel","city","city","Property city","StringProperty",True).put()
metaModel("jsonModel","corelogic_collateral_risk_score","CoreLogic Collateral Risk Score","CoreLogic Collateral Risk Score","IntegerProperty",True).put()
metaModel("jsonModel","corelogic_fraud_risk_score","CoreLogic Fraud Risk Score","CoreLogic Fraud Risk Score","IntegerProperty",True).put()
metaModel("jsonModel","cur_note_rate","Cur_note_rate","Current note rate","FloatProperty",True).put()
metaModel("jsonModel","curr_upb","curr_upb","Current Unpaid Balance","IntegerProperty",True).put()
metaModel("jsonModel","debt_service_ratio","debt_service_ratio","debt service ratio","FloatProperty",True).put()
metaModel("jsonModel","doc_level_code","doc_level_code","Document Level Code","IntegerProperty",True).put()
metaModel("jsonModel","du_case_number","du_case_number","du case number","IntegerProperty",True,1000100100).put()
metaModel("jsonModel","du_response","du_response","du response","StringProperty",True).put()
metaModel("jsonModel","effective_date","effective_date","Request Date","DateProperty",True).put()
metaModel("jsonModel","fha_case_number","FHA_Case_Number","FHA Case Number","StringProperty").put()
metaModel("jsonModel","fico_score","fico_score","fico score","IntegerProperty",True).put()
metaModel("jsonModel","first_adj_max_initial_rate","1st_adj_max_initial_rate","1st adjustment maximum initial rate","FloatProperty").put()
metaModel("jsonModel","first_adj_min_initial_rate","1st_adj_min_initial_rate","1st adjustment minimum initial rate","FloatProperty").put()
metaModel("jsonModel","first_delinquent_date","first_delinquent_date","first delinquent date","DateProperty").put()
metaModel("jsonModel","first_payment_change_date","First_payment_change_date","First payment change date","DateProperty").put()
metaModel("jsonModel","first_rate_adjust_period","first_rate_adjust_period","first rate adjustment period","IntegerProperty").put()
metaModel("jsonModel","first_rate_change_date","first_rate_change_date","first rate change date","DateProperty").put()
metaModel("jsonModel","firstdue","firstdue","first payment due date","DateProperty",True,"2/1/2012").put()
metaModel("jsonModel","foreclosure_satisfied_date","foreclosure_satisfied_date","foreclosure satisfied date","DateProperty").put()
metaModel("jsonModel","funding_amount","funding_amount","Amount Sent","FloatProperty").put()
metaModel("jsonModel","funding_id","funding_id","funding id","IntegerProperty").put()
metaModel("jsonModel","funding_method_code","funding_method_code","funding method code","IntegerProperty",True,1).put()
metaModel("jsonModel","initial_recast_period","Initial_recast_period","Initial recast period","IntegerProperty").put()
metaModel("jsonModel","interest_only_end_date","Interest_Only_End_Date","Interest Only End Date","DateProperty").put()
metaModel("jsonModel","interest_only_flag","interest_only_flag","interest only flag","BooleanProperty",True,False).put()
metaModel("jsonModel","interest_only_period","interest_only_period","interest only  period","IntegerProperty",True,0).put()
metaModel("jsonModel","interest_rounding_feature","Interest_rounding_feature","Interest rounding feature","StringProperty").put()
metaModel("jsonModel","interest_rounding_percentage","Interest_rounding_percentage","Interest rounding percentage","FloatProperty").put()
metaModel("jsonModel","inv_commit_date","inv_commit_date","Investor Commitment Date","DateProperty",True).put()
metaModel("jsonModel","inv_commit_expire_date","inv_commit_expire_date","Investor Commitment Expire Date","DateProperty",True).put()
metaModel("jsonModel","inv_commit_number","inv_commit_number","Investor Commitment Number","IntegerProperty",True).put()
metaModel("jsonModel","inv_commit_price","inv_commit_price","Investor Commitment Price","IntegerProperty",True,100).put()
metaModel("jsonModel","investor_code","investor_code","investor code","StringProperty",True).put()
metaModel("jsonModel","investor_id","investor_id","investor id","StringProperty").put()
metaModel("jsonModel","is_adjustable","is_adjustable","is interest rate adjustable?","BooleanProperty",True).put()
metaModel("jsonModel","is_assets_verified","is_assets_verified","Assets verified?","BooleanProperty",True,True).put()
metaModel("jsonModel","is_balloon","Is_balloon","Is loan a balloon?","BooleanProperty",True,False).put()
metaModel("jsonModel","is_escrow_required","is_escrow_required","is escrow required?","BooleanProperty",True).put()
metaModel("jsonModel","is_first_time_buyer","is_first_time_buyer","is first time buyer?","BooleanProperty",True,False).put()
metaModel("jsonModel","is_lpmi","Is_LPMI","Is LPMI","BooleanProperty",True,False).put()
metaModel("jsonModel","is_negam","is_negam","is loan negatively amortizing?","BooleanProperty",True,False).put()
metaModel("jsonModel","junior_lien_amount","Junior_lien_amount","Junior lien amount","IntegerProperty",True,0).put()
metaModel("jsonModel","lien_position","lien_position","lien position","IntegerProperty",True).put()
metaModel("jsonModel","loan_officer","Loan Officer","Loan Officer","StringProperty",True).put()
metaModel("jsonModel","loan_type","Loan_Type","Loan Type","StringProperty",True).put()
metaModel("jsonModel","look_back_period","Look_back_period","Look back period","IntegerProperty").put()
metaModel("jsonModel","lpmi_pct","LPMI_PCT","LPMI Percentage","FloatProperty",True,False).put()
metaModel("jsonModel","market_value_cap","Market_value_cap","Market value cap","IntegerProperty",True,100).put()
metaModel("jsonModel","maturity","maturity","maturity date","DateProperty",True).put()
metaModel("jsonModel","max_negam","max_negam","maximum negatively amortization","FloatProperty",True,0).put()
metaModel("jsonModel","max_rate","Max_Rate","Max Rate","FloatProperty").put()
metaModel("jsonModel","mers_min","mers_min","mers min number","StringProperty",True,100000000000000000).put()
metaModel("jsonModel","mo_city","MO City","MO City","StringProperty",True).put()
metaModel("jsonModel","mo_state","MO State","MO State","StringProperty").put()
metaModel("jsonModel","mo_zip","MO Zip","MO Zip","StringProperty").put()
metaModel("jsonModel","mtg_ins_company","mtg_ins_company","mortgage insurance company","StringProperty").put()
metaModel("jsonModel","mtg_ins_pct","mtg_ins_pct","Mortgage Insurance","BooleanProperty",True,0).put()
metaModel("jsonModel","nmls_n","NMLS #","NMLS #","IntegerProperty",True).put()
metaModel("jsonModel","occupancy_code","occupancy_code","occupancy code","StringProperty",True).put()
metaModel("jsonModel","orig_appraised_value","orig_appraised_value","original appraised value","IntegerProperty",True).put()
metaModel("jsonModel","orig_p_i","orig_p_i","Original Principal & Interest Payment","FloatProperty",True).put()
metaModel("jsonModel","orig_rate","orig_rate","Original Interest Rate","FloatProperty",True).put()
metaModel("jsonModel","orig_upb","orig_upb","Original Unpaid Balance","IntegerProperty",True).put()
metaModel("jsonModel","original_cltv","original_cltv","original cltv","FloatProperty",True).put()
metaModel("jsonModel","original_ltv","original_ltv","original ltv","FloatProperty",True).put()
metaModel("jsonModel","original_term","original_term","original term","IntegerProperty",True).put()
metaModel("jsonModel","origination_date","origination_date","origination date","DateProperty",True).put()
metaModel("jsonModel","paid_to_date","paid_to_date","paid to date","DateProperty",True,"1/1/2012").put()
metaModel("jsonModel","payee1_abanum","payee1_abanum","1st payee ABA number","StringProperty").put()
metaModel("jsonModel","payee1_accountnum","payee1_accountnum","1st payee account number","StringProperty").put()
metaModel("jsonModel","payee1_address","payee1_address","1st Payee Address","StringProperty").put()
metaModel("jsonModel","payee1_city","payee1_city","1st Payee City","StringProperty",True).put()
metaModel("jsonModel","payee1_instruction1","payee1_instruction1","1st Payee Wire Instruction 1","StringProperty").put()
metaModel("jsonModel","payee1_instruction2","payee1_instruction2","1st Payee Wire Instruction 2","StringProperty").put()
metaModel("jsonModel","payee1_name","payee1_name","1st Payee Name","StringProperty",True).put()
metaModel("jsonModel","payee1_state","payee1_state","1st Payee State","StringProperty",True).put()
metaModel("jsonModel","payee1_zip","payee1_zip","1st Payee Zip","StringProperty",True).put()
metaModel("jsonModel","payee2_abanum","payee2_abanum","2nd payee ABA number","StringProperty").put()
metaModel("jsonModel","payee2_accountnum","payee2_accountnum","2nd payee account number","StringProperty").put()
metaModel("jsonModel","payee2_address","payee2_address","2nd Payee Address","StringProperty").put()
metaModel("jsonModel","payee2_city","payee2_city","2nd Payee City","StringProperty").put()
metaModel("jsonModel","payee2_instruction1","payee2_instruction1","2nd Payee Wire Instruction 1","StringProperty").put()
metaModel("jsonModel","payee2_instruction2","payee2_instruction2","2nd Payee Wire Instruction 2","StringProperty").put()
metaModel("jsonModel","payee2_name","payee2_name","2nd Payee Name","StringProperty").put()
metaModel("jsonModel","payee2_state","payee2_state","2nd Payee State","StringProperty").put()
metaModel("jsonModel","payee2_zip","payee2_zip","2nd Payee Zip","StringProperty").put()
metaModel("jsonModel","prepay_enforceability","prepay_enforceability","prepay enforceability","StringProperty").put()
metaModel("jsonModel","prepay_penalty_flag","prepay_penalty_flag","prepayment penalty flag","BooleanProperty",True,False).put()
metaModel("jsonModel","prepay_penalty_pct","prepay_penalty_pct","prepayment penalty percentage","FloatProperty",True,0).put()
metaModel("jsonModel","prepay_period","prepay_period","prepayment period","StringProperty").put()
metaModel("jsonModel","product_code","product_code","Loan Type","StringProperty",True).put()
metaModel("jsonModel","property_type_code","property_type_code","property type code","StringProperty",True).put()
metaModel("jsonModel","purchase_price","purchase_price","purchase price","IntegerProperty",True).put()
metaModel("jsonModel","purpose_code","purpose_code","purpose code","StringProperty",True).put()
metaModel("jsonModel","rate_change_frequency","rate_change_frequency","rate adjustment frequency","IntegerProperty").put()
metaModel("jsonModel","reserved_amt","reserved_amt","reserved amount","FloatProperty",True).put()
metaModel("jsonModel","reserved_term","reserved_term","reserved term","IntegerProperty",True).put()
metaModel("jsonModel","servicer","Servicer","Servicer","StringProperty").put()
metaModel("jsonModel","servicing_fee","Servicing_fee","Servicing fee","FloatProperty",True,0).put()
metaModel("jsonModel","ss_number","ss_number","SS# (Primary Borrower)","IntegerProperty",True).put()
metaModel("jsonModel","ss_number_2","ss_number_2","SS# (Secondary Borrower)","IntegerProperty").put()
metaModel("jsonModel","state","state","Property state","StringProperty",True).put()
metaModel("jsonModel","subsequent_recast_period","subsequent_recast_period","subsequent recast period","IntegerProperty").put()
metaModel("jsonModel","teaser_period","teaser_period","teaser period","IntegerProperty").put()
metaModel("jsonModel","times_delinquent_120","times_delinquent_120","times delinquent 120","IntegerProperty",True,0).put()
metaModel("jsonModel","times_delinquent_30","times_delinquent_30","times delinquent 30","IntegerProperty",True,0).put()
metaModel("jsonModel","times_delinquent_60","times_delinquent_60","times delinquent 60","IntegerProperty",True,0).put()
metaModel("jsonModel","times_delinquent_90","times_delinquent_90","times delinquent 90","IntegerProperty",True,0).put()
metaModel("jsonModel","tradelines","tradelines","tradelines","IntegerProperty",True).put()
metaModel("jsonModel","u_w","U/W","Loan Underwriter","StringProperty",True).put()
metaModel("jsonModel","units","units","units","IntegerProperty",True,1).put()
metaModel("jsonModel","pzip","zip","Property zip","StringProperty",True).put()