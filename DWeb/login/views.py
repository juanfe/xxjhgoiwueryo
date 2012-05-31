## \file login\view.py
## \brief Views for the Liquidity Spot authentication system

from django import forms
from forms import LiqSpotUserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import UserInGroup

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin"]),
		        login_url='/accounts/login/?next=/accounts/register/')
def register(request):
	if request.method == 'POST':
		form = LiqSpotUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = LiqSpotUserCreationForm()
	return render_to_response("registration/register.html", {'form': form,})
