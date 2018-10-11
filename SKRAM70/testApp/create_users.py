from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Profile, Customers, Stores, StaffMembers

def CreateUsers():
    User.objects.all().delete()
    Group.objects.all().delete()
    Permission.objects.all().delete()
    staffUser = User.objects.create_user(username='staff', email='abc@example.com', password='1234')
    staffUser_1 = User.objects.create_user(username='staff1', email='abc@example.com', password='1234')
    customerUser = User.objects.create_user(username='customer', email='abc@example.com', password='1234')
    customerUser_1 = User.objects.create_user(username='customer1', email='abc@example.com', password='1234')
    boardMemberUser = User.objects.create_user(username='BM', email='abc@example.com', password='1234')

    staff_group, created = Group.objects.get_or_create(name='staff_group')
    ct = ContentType.objects.get_for_model(User)
    staff_permission = Permission.objects.create(codename='staff_member',
                                   name='Staff Member',
                                   content_type = ct)
    staff_group.permissions.add(staff_permission)
    staff_group.user_set.add(staffUser)
    staff_group.user_set.add(staffUser_1)

    storeObject = Stores.objects.get(id=1)
    staffMember = StaffMembers(user=staffUser, storeid=storeObject)
    staffMember.save()

    storeObject = Stores.objects.get(id=2)
    staffMember = StaffMembers(user=staffUser_1, storeid=storeObject)
    staffMember.save()

    boardMember_group, created = Group.objects.get_or_create(name='boardMember_group')
    boardMember_permission = Permission.objects.create(codename='board_member',
                                   name='Board Member',
                                   content_type = ct)
    boardMember_group.permissions.add(boardMember_permission)
    boardMember_group.user_set.add(boardMemberUser)

    customer_group, created = Group.objects.get_or_create(name='customer_group')
    customer_permission = Permission.objects.create(codename='customer',
                                   name='Customer',
                                   content_type = ct)
    customer_group.permissions.add(customer_permission)
    customer_group.user_set.add(customerUser)
    customer_group.user_set.add(customerUser_1)

    customerObject = Customers.objects.get(id=11010)
    customer = Profile(user=customerUser, customerid=customerObject)
    customer.save()

    customerObject = Customers.objects.get(id=11011)
    customer = Profile(user=customerUser_1, customerid=customerObject)
    customer.save()
