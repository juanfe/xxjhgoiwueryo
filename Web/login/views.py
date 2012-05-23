from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#Imports to test login_view
from django.contrib import auth
from django.http import HttpResponse

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/accounts/login/")
	else:
		form = UserCreationForm()
	return render_to_response("registration/register.html", {'form': form,})
