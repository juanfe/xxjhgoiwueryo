## \file initial_data\view.py
## \brief Initial data load.

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from permission_backend_nonrel import utils

def load_data(request):
	#Groups of users
	#TODO check if there are no groups
	admin = Group(name="Admin")
	mo = Group(name="MO")
	broker = Group(name="Broker")
	engine = Group(name="Engine")
	admin.save()
	mo.save()
	broker.save()
	engine.save()

	#TODO change this by functionality of admin
	user_admin = User.objects.create_user('Admin', 'Admin@liqspot.com',
			'Vichara')
	user_admin.is_staff = True
	user_admin.save()
	#user_admin.groups.add(admin)
	utils.add_user_to_group(user_admin, admin)

	#Creating Mortgage Operators Users
	user = User.objects.create_user('ABC Mortgage', 'ABC_Mortgage@tempo.com',
			'1234')
	user.is_staff = True
	user.save()
	#user.groups.add(mo)
	utils.add_user_to_group(user, mo)

	user = User.objects.create_user('Prime Lending', 'Prime_Lending@tempo.com',
			'1234')
	user.is_staff = True
	user.save()
	#user.groups.add(mo)
	utils.add_user_to_group(user, mo)

	user = User.objects.create_user('Best Loans Inc', 'Best_Loans_Inc@tempo.com',
			'1234')
	user.is_staff = True
	user.save()
	#user.groups.add(mo)
	utils.add_user_to_group(user, mo)

	user = User.objects.create_user('Integrity Lending', 'Integrity_Lending@tempo.com',
			'1234')
	user.is_staff = True
	user.save()
	#user.groups.add(mo)
	utils.add_user_to_group(user, mo)

	return HttpResponse("Data had been loaded")
