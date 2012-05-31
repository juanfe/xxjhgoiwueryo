from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import FundsCashFlow 

class FundsForm(ModelForm):
	class Meta:
		model = FundsCashFlow

	def __init__(self, *args, **kwargs):
		super (FundsForm, self).__init__(*args, **kwargs)
		#TODO filter by 'Broker'
		self.fields['User'].queryset = User.objects.all()
