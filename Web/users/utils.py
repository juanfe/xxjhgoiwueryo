from django.contrib.auth.models import User, Group
from permission_backend_nonrel.models import UserPermissionList

def UserInGroup(User, groupName):
	group = Group.objects.get(name=groupName)
	up = UserPermissionList.objects.filter(user = User)
	try:
		return True if unicode(group.id) in up[0].group_fk_list else False
	except:
		return False
