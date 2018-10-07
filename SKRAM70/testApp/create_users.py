from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

def CreateUsers():
    User.objects.all().delete()
    Group.objects.all().delete()
    Permission.objects.all().delete()
    staffUser = User.objects.create_user(username='staff', email='abc@example.com', password='1234')
    customerUser = User.objects.create_user(username='customer', email='abc@example.com', password='1234')
    boardMemberUser = User.objects.create_user(username='BM', email='abc@example.com', password='1234')

    staff_group = Group.objects.get_or_create(name='staff_group')
    ct = ContentType.objects.get_for_model(User)
    staff_permission = Permission.objects.create(codename='staff_member',
                                   name='Staff Member',
                                   content_type = ct)
    staff_group.permissions.add(staff_permission)
    staff_group.user_set.add(staffUser)

    boardMember_group = Group.object.get_or_create(name='boardMember_group')
    boardMember_permission = Permission.objects.create(codename='board_member',
                                   name='Board Member',
                                   content_type = ct)
    staff_group.permissions.add(boardMember_permission)
    staff_group.user_set.add(boardMemberUser)
