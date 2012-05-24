## \file initial_data\view.py
## \brief Initial data load.

from django.contrib.auth.models import User, Group

def load_data(request):
	#Groups of users
	admin = Group(name="Admin")
	mo = Group(name="MO")
	broker = Group(name="Broker")
	engine = Group(name="Engine")
	admin.save()
	mo.save()
	broker.save()
	engine.save()

	return HttpResponse("Data had been loaded")
