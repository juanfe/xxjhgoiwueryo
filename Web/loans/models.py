import moneyed
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.db import models
from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from datetime import datetime

class MortgageOriginator(models.Model):
	Name = models.CharField(max_length=200)
	#TODO add user as foreignkey to contact
	#Contact = models.ForeignKey(User)

	def __unicode__(self):
		return self.Name

	#def create_MortgageOriginator(user)
	#	Name = user
	#	Contact = User.objects.get(username = user)

class Loan(models.Model):
	#TODO look for what means each code
	lastkey = 0
	INVESTOR_CODE_CHOICES = (
		('BOAM', 'BOAM'),
		('FNMA', 'FNMA'),
		('GMAC', 'GMAC'),
		('JPM', 'JPM'),
	)
	PROPERTY_TYPE_CODE = (
		('SFR', 'SFR'),
		('PUB', 'PUB'),
	)
	LIEN_POSITION_CHOICES = (
		(1, 1),
		(2, 2),
	)
	PURPOSE_CODE_CHOICES = (
		('CO', 'CO'),
		('P', 'P'),
		('R', 'R'),
	)
	OCCUPANCY_CODE_CHOICES = (
		('O', 'O'),
		('I', 'I'),
		('S', 'S'),
	)
	DOC_LEVEL_CODE_CHOICES = (
			( 1, 1),
			( 3, 3),
	)
	#TODO  add: db_index=true, foreign key 
	key_name = models.CharField( max_length=80, verbose_name="Key", primary_key=True,
			db_column = "Key")
	customer_account_key = models.CharField(max_length=80, db_column="MO Name",
			verbose_name="Mortgage Originator")
	collateral_key = models.CharField(max_length=80, verbose_name="Loan Number")
	#Loan Amount
	#advance_amt = MoneyField(max_digits = 20, decimal_places = 9, verbose_name="MO advance amount",
	#		default_currency=moneyed.USD)
	advance_amt = models.FloatField(verbose_name="MO advance amount")
	advance_amtDate = models.DateTimeField(auto_now = True, null = True)
	state = USStateField(choices=STATE_CHOICES, verbose_name="Property state")
	pzip = models.CharField(max_length=10, verbose_name="Property zip")
	#orig_upb = MoneyField(max_digits = 20, decimal_places = 9,
	#		verbose_name="Original Unpaid Balance",
	#		default_currency=moneyed.USD)
	orig_upb = models.FloatField(verbose_name="Original Unpaid Balance")
	orig_upbDate = models.DateTimeField(auto_now=True, null = True)
	#curr_upb = MoneyField(max_digits = 20, decimal_places = 9,
	#		verbose_name="Current Unpaid Balance",
	#		default_currency=moneyed.USD)
	curr_upb = models.FloatField(verbose_name="Current Unpaid Balance")
	curr_upbDate = models.DateTimeField(auto_now=True, null = True)
	# Creation date
	origination_date = models.DateTimeField(auto_now=True, verbose_name="origination date", null = True)
	is_adjustable = models.BooleanField(verbose_name="is interest rate adjustable?")
	##TODO X divided by P
	investor_code = models.CharField(max_length=80, verbose_name="investor code", 
			choices = INVESTOR_CODE_CHOICES)
	property_type_code = models.CharField(max_length=80, verbose_name="property type code",
			choices = PROPERTY_TYPE_CODE)
	lien_position = models.DecimalField(max_digits = 1, decimal_places = 0, verbose_name="lien position",
			choices = LIEN_POSITION_CHOICES)
	original_ltv = models.DecimalField(max_digits = 10, decimal_places = 7, verbose_name="original ltv")
	original_cltv = models.DecimalField(max_digits = 10, decimal_places = 7, verbose_name="original cltv")
	fico_score = models.DecimalField(max_digits = 4, decimal_places = 0, verbose_name="fico score")
	purpose_code = models.CharField(max_length=80, verbose_name="purpose code",
			choices = PURPOSE_CODE_CHOICES)
	occupancy_code = models.CharField(max_length=80, verbose_name="occupancy code",
			choices = OCCUPANCY_CODE_CHOICES)
	doc_level_code = models.DecimalField(max_digits = 1, decimal_places = 0,
			verbose_name="Document Level Code", choices = DOC_LEVEL_CODE_CHOICES)
	debt_service_ratio = models.DecimalField(max_digits = 10, decimal_places = 7,
			verbose_name="debt service ratio")
	cur_note_rate = models.DecimalField(max_digits = 10, decimal_places = 7,
			verbose_name="Current note rate")
	#TODO ask by the range of the Fraud risk score, may be VAR?
	corelogic_fraud_risk_score = models.DecimalField(max_digits = 4, decimal_places = 0,
			verbose_name="CoreLogic Fraud Risk Score")
	corelogic_collateral_risk_score = models.DecimalField(max_digits = 4,
			decimal_places = 0, verbose_name="CoreLogic Collateral Risk Score")
	Hiden = models.BooleanField()

	#  This field are from the file 'Funding File - Definitions Template w dummy
	#  data.xlsx
	#address = models.CharField(max_length=80, verbose_name="Property address")
	#amortization_term = models.DecimalField(verbose_name="amortization term")
	#anncap_init = models.DecimalField(verbose_name="Initial Rate Adjustment Cap")
	#appraiser_name = models.CharField(max_length=80, verbose_name="appraiser name")
	#armindex = models.CharField(max_length=80, verbose_name="ARM Index")
	#armlcap = models.DecimalField(verbose_name="Lifetime Rate Adjustment Cap")
	#armlfloor = db.FloatProperty(verbose_name="Lifetime Floor Rate")
	#armmargin = db.FloatProperty(verbose_name="ARM Margin")
	#armoption = db.BooleanProperty(verbose_name="is loan an Option ARM?",default=False)
	#armpcap = models.DecimalField(verbose_name="Periodic Rate Adjustment Cap")
	#armpfloor = models.DecimalField(verbose_name="Periodic Rate Cap")
	#armteaser = db.FloatProperty(verbose_name="ARM Teaser")
	#bankruptcy_chapter = models.CharField(max_length=80, verbose_name="bankruptcy chapter")
	#bankruptcy_discharge_date = db.DateProperty(verbose_name="bankruptcy discharge date")
	#borr_1_age = models.DecimalField(verbose_name="Primary borrower age")
	#borr_1_employ_flag = db.BooleanProperty(verbose_name="Primary borrower employment flag")
	#borr_1_first_name = models.CharField(max_length=80, verbose_name="First Name (Primary Borrower)")
	#borr_1_gender = models.CharField(max_length=80, verbose_name="Primary borrower Gender",choices=set(["M","F"]))
	#borr_1_last_name = models.CharField(max_length=80, verbose_name="Last Name (Primary Borrower)")
	#borr_1_marital_status = models.CharField(max_length=80, verbose_name="Primary borrower marital status")
	#borr_2_age = models.DecimalField(verbose_name="Secondary borrower age")
	#borr_2_employ_flag = db.BooleanProperty(verbose_name="Secondary Borrower employment flag")
	#borr_2_first_name = models.CharField(max_length=80, verbose_name="First Name (Secondary Borrower)")
	#borr_2_gender = models.CharField(max_length=80, verbose_name="Secondary borrower gender",choices=set(["M","F"]))
	#borr_2_last_name = models.CharField(max_length=80, verbose_name="Last Name (Secondary Borrower)")
	#borr_2_marital_status = models.CharField(max_length=80, verbose_name="Secondary borrower marital status")
	#citizenship_flag = db.BooleanProperty(verbose_name="Citizen Y/N")
	#city = models.CharField(max_length=80, verbose_name="Property city")
	#du_case_number = models.DecimalField(verbose_name="du case number",default="1000100100")
	#du_response = models.CharField(max_length=80, verbose_name="du response")
	#effective_date = db.DateProperty(verbose_name="Request Date")
	#fha_case_number = models.CharField(max_length=80, verbose_name="FHA Case Number")
	#first_adj_max_initial_rate = db.FloatProperty(verbose_name="1st adjustment maximum initial rate")
	#first_adj_min_initial_rate = db.FloatProperty(verbose_name="1st adjustment minimum initial rate")
	#first_delinquent_date = db.DateProperty(verbose_name="first delinquent date")
	#first_payment_change_date = db.DateProperty(verbose_name="First payment change date")
	#first_rate_adjust_period = models.DecimalField(verbose_name="first rate adjustment period")
	#first_rate_change_date = db.DateProperty(verbose_name="first rate change date")
	#firstdue = db.DateProperty(verbose_name="first payment due date"
	#		,default=datetime.strptime("2/1/2012","%m/%d/%Y").date())
	#foreclosure_satisfied_date = db.DateProperty(verbose_name="foreclosure satisfied date")
	#funding_amount = db.FloatProperty(verbose_name="Amount Sent")
	#funding_id = models.DecimalField(verbose_name="funding id")
	#funding_method_code = models.DecimalField(verbose_name="funding method code",default=1)
	#initial_recast_period = models.DecimalField(verbose_name="Initial recast period")
	#interest_only_end_date = db.DateProperty(verbose_name="Interest Only End Date")
	#interest_only_flag = db.BooleanProperty(verbose_name="interest only flag",default=False)
	#interest_only_period = models.DecimalField(verbose_name="interest only  period",default=0)
	#interest_rounding_feature = models.CharField(max_length=80, verbose_name="Interest rounding feature")
	#interest_rounding_percentage = db.FloatProperty(verbose_name="Interest rounding percentage")
	#inv_commit_date = db.DateProperty(verbose_name="Investor Commitment Date")
	#inv_commit_expire_date = db.DateProperty(verbose_name="Investor Commitment Expire Date")
	#inv_commit_number = models.DecimalField(verbose_name="Investor Commitment Number")
	#inv_commit_price = models.DecimalField(verbose_name="Investor Commitment Price",default=100)
	#investor_id = models.CharField(max_length=80, verbose_name="investor id")
	#is_assets_verified = db.BooleanProperty(verbose_name="Assets verified?",default=True)
	#is_balloon = db.BooleanProperty(verbose_name="Is loan a balloon?",default=False)
	#is_escrow_required = db.BooleanProperty(verbose_name="is escrow required?")
	#is_first_time_buyer = db.BooleanProperty(verbose_name="is first time buyer?",default=False)
	#is_lpmi = db.BooleanProperty(verbose_name="Is LPMI",default=False)
	#is_negam = db.BooleanProperty(verbose_name="is loan negatively amortizing?",default=False)
	#junior_lien_amount = models.DecimalField(verbose_name="Junior lien amount",default=0)
	#loan_officer = models.CharField(max_length=80, verbose_name="Loan Officer")
	#loan_type = models.CharField(max_length=80, verbose_name="Loan Type")
	#look_back_period = models.DecimalField(verbose_name="Look back period")
	#lpmi_pct = db.FloatProperty(verbose_name="LPMI Percentage",default=0.0)
	#market_value_cap = models.DecimalField(verbose_name="Market value cap",default=100)
	#maturity = db.DateProperty(verbose_name="maturity date")
	#max_negam = db.FloatProperty(verbose_name="maximum negatively amortization",default=0)
	#max_rate = db.FloatProperty(verbose_name="Max Rate")
	#mers_min = models.CharField(max_length=80, verbose_name="mers min number",default="100000000000000000")
	#mo_city = models.CharField(max_length=80, verbose_name="MO City")
	#mo_state = USStateField(choices=STATE_CHOICES,
	#		verbose_name="Property state", verbose_name="MO State")
	#mo_zip = models.models.CharField(max_length=10, verbose_name="MO Zip")
	#mtg_ins_company = models.CharField(max_length=80, verbose_name="mortgage insurance company")
	#mtg_ins_pct = db.BooleanProperty(verbose_name="Mortgage Insurance",default=False)
	#nmls_n = models.DecimalField(verbose_name="NMLS #")
	#orig_appraised_value = models.DecimalField(verbose_name="original appraised value")
	#orig_p_i = db.FloatProperty(verbose_name="Original Principal & Interest Payment")
	#orig_rate = db.FloatProperty(verbose_name="Original Interest Rate")
	#original_term = models.DecimalField(verbose_name="original term")
	#paid_to_date = db.DateProperty(verbose_name="paid to date",
	#		default=datetime.strptime("1/1/2012","%m/%d/%Y").date())
	#payee1_abanum = models.CharField(max_length=80, verbose_name="1st payee ABA number")
	#payee1_accountnum = models.CharField(max_length=80, verbose_name="1st payee account number")
	#payee1_address = models.CharField(max_length=80, verbose_name="1st Payee Address")
	#payee1_address = models.CharField(max_length=80, verbose_name="1st Payee Address")
	#payee1_city = models.CharField(max_length=80, verbose_name="1st Payee City")
	#payee1_instruction1 = models.CharField(max_length=80, verbose_name="1st Payee Wire Instruction 1")
	#payee1_instruction2 = models.CharField(max_length=80, verbose_name="1st Payee Wire Instruction 2")
	#payee1_name = models.CharField(max_length=80, verbose_name="1st Payee Name")
	#payee1_state = USStateField(choices=STATE_CHOICES,
	#		verbose_name="Property state", verbose_name="1st Payee State")
	#payee1_zip = models.models.CharField(max_length=10, verbose_name="1st Payee Zip")
	#payee2_abanum = models.CharField(max_length=80, verbose_name="2nd payee ABA number")
	#payee2_accountnum = models.CharField(max_length=80, verbose_name="2nd payee account number")
	#payee2_address = models.CharField(max_length=80, verbose_name="2nd Payee Address")
	#payee2_city = models.CharField(max_length=80, verbose_name="2nd Payee City")
	#payee2_instruction1 = models.CharField(max_length=80, verbose_name="2nd Payee Wire Instruction 1")
	#payee2_instruction2 = models.CharField(max_length=80, verbose_name="2nd Payee Wire Instruction 2")
	#payee2_name = models.CharField(max_length=80, verbose_name="2nd Payee Name")
	#payee2_state = USStateField(choices=STATE_CHOICES,
	#		verbose_name="Property state", verbose_name="2st Payee State")
	#payee2_zip = models.models.CharField(max_length=10, verbose_name="2st Payee Zip")
	#prepay_enforceability = models.CharField(max_length=80, verbose_name="prepay enforceability")
	#prepay_penalty_flag = db.BooleanProperty(verbose_name="prepayment penalty flag",default=False)
	#prepay_penalty_pct = db.FloatProperty(verbose_name="prepayment penalty
	#percentage",default=0.0)
	#prepay_period = models.CharField(max_length=80, verbose_name="prepayment period")
	#product_code = models.CharField(max_length=80, verbose_name="Loan Type")
	#purchase_price = models.DecimalField(verbose_name="purchase price")
	#rate_change_frequency = models.DecimalField(verbose_name="rate adjustment frequency")
	#reserved_amt = db.FloatProperty(verbose_name="reserved amount")
	#reserved_term = models.DecimalField(verbose_name="reserved term")
	#servicer = models.CharField(max_length=80, verbose_name="Servicer")
	#servicing_fee = db.FloatProperty(verbose_name="Servicing fee",default=0.0)
	#ss_number = models.CharField(max_length=80, verbose_name="SS# (Primary Borrower)")
	#ss_number_2 = models.CharField(max_length=80, verbose_name="SS# (Secondary Borrower)")
	#subsequent_recast_period = models.DecimalField(verbose_name="subsequent recast period")
	#teaser_period = models.DecimalField(verbose_name="teaser period")
	#times_delinquent_30 = models.DecimalField(verbose_name="times delinquent 30",default=0)
	#times_delinquent_60 = models.DecimalField(verbose_name="times delinquent 60",default=0)
	#times_delinquent_90 = models.DecimalField(verbose_name="times delinquent 90",default=0)
	#times_delinquent_120 = models.DecimalField(verbose_name="times delinquent 120",default=0)
	#tradelines = models.DecimalField(verbose_name="tradelines")
	#u_w = models.CharField(max_length=80, verbose_name="Loan Underwriter")
	#units = models.DecimalField(verbose_name="units",default=1)

	#  The next field, could be the same as fistdue, was created by Camilo
	#Assignation = models.DateTimeField()

	#def __init__(self, *args, **kwargs):
	##TODO Make a function to add an automatic primary key if it is not supplied
	#	if not kwargs.has_key("key_name") and args == ():
	#		self.lastkey += 1 
	#		self.key_name = "Vichara%s" % self.lastkey
	#	super(models.Model, self).__init__(*args, **kwargs)
