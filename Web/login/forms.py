from django import forms
from django.contrib.auth.forms import UserCreationForm

GROUP_CHOICES = (
	('MO', 'Mortgage Originator'),
	('Broker', 'Bids Originator'),
)

class LiqSpotUserCreationForm(UserCreationForm):
	receive_newsletter = forms.ChoiceField(choices=GROUP_CHOICES)
