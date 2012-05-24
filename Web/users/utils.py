## \file users\utils.py
## \brief Utilities to check users qualities

from django.contrib.auth.models import User, Group
from permission_backend_nonrel.models import UserPermissionList

def UserInGroup(User, groupList):
	"""\brief Function to check if a user belong to any of the groups in list.

	\param User to be checked if exist in the list \a groupList
	\param groupList is a list of group's names
	"""
	#TODO allow many check many groups
	gids = []
	try:
		for g in Group.objects.filter(name__in=groupList):
			gids.append(unicode(g.id))
		up = UserPermissionList.objects.filter(user = User)
		return True if len(set(gids).intersection(set(up[0].group_fk_list))) > 0 else False
	except:
		return False
