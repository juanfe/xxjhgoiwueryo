## \file login\view.py
## \brief Views for the Liquidity Spot authentication system

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

gin_required
@user_passes_test(lambda u: UserInGroup(u, "Admin"),
		        login_url='/accounts/login/?next=/accounts/register/')
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			#return HttpResponseRedirect("/")
			return HttpResponse("User had been registered")
	else:
		form = UserCreationForm()
	return render_to_response("registration/register.html", {'form': form,})
