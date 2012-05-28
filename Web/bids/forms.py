from django.forms import ModelForm
from bids.models import Bid

class BidForm(ModelForm):
	class Meta:
		model = Bid
		exclude = ('FundsAvailable')
