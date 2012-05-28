from django import forms
from django.contrib.auth.forms import UserCreationForm

GROUP_CHOICES = (
	('MO', 'Mortgage Originator'),
	('Broker', 'Bids Originator'),
)

class LiqSpotUserCreationForm(UserCreationForm):
	lsgroup = forms.ChoiceField(choices=GROUP_CHOICES)
	#TODO add __init__ and add groups to User
