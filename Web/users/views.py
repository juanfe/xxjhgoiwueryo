from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import UserInGroup
from users.models import FundsCashFlow

@login_required
@user_passes_test(lambda u: UserInGroup(u, ["Admin"]),
		login_url='/accounts/login/?next=/bids/bids/')
def funds(request):
	users_funds = FundsCashFlow.objects.all()

	return render_to_response('users/formfunds.html',
			{'users_funds': users_funds},
			context_instance=RequestContext(request))
