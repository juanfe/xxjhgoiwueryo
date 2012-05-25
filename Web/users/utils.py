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
		gids = (unicode(g.id) for g in Group.objects.filter(name__in=groupList))
		up = UserPermissionList.objects.filter(user = User)
		return True if len(set(gids).intersection(set(up[0].group_fk_list))) > 0 else False
	except:
		return False

def is_logged_in(request):
	return request.user.is_authenticated()

def UserName(request):
	return str(request.user)

def GetUserGroups(request):
	try:
		User = request.user
		g_ids = UserPermissionList.objects.filter(user = User)[0].group_fk_list
		g_lst = Group.objects.filter(id__in = g_ids)
		return [str(g) for g in g_lst]
	except:
		return []
