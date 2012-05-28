from django.forms import ModelForm
from users.models import FundsCashFlow 

class FundsForm(ModelForm):
	class Meta:
		model = FundsCashFlow
