from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from ..models import *

def CreateUsers():
    staffUser = User.objects.create_user(username='staff', email='abc@example.com', password='1234')
    customerUser = User.objects.create_user(username='customer', email='abc@example.com', password='1234')
    boardMemberUser = User.objects.create_user(username='BM', email='abc@example.com', password='1234')

    staff_group, created = Group.objects.get_or_create(name='staff_group')
    ct = ContentType.objects.get_for_model(User)
    staff_permission = Permission.objects.create(codename='staff_member',
                                   name='Staff Member',
                                   content_type = ct)
    staff_group.permissions.add(staff_permission)
    staff_group.user_set.add(staffUser)

    Stores.objects.create(name = "testName",
        address = "testAdress",
        phone = "045555555",
        city = "testCity",
        state = "testState")

    for storeObject in Stores.objects.all():
        StaffMembers.objects.create(user=staffUser, storeid=storeObject)

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

    Customers.objects.create(name='Kaushal Kishorbhai Limbasiya',
    phone = 1234567890,
    dob = 19970909,
    email = 'abcd@gmail.com',
    password = 'abcd1234')

    for customerObject in Customers.objects.all():
        Profile.objects.create(user = customerUser, customerid = customerObject)
