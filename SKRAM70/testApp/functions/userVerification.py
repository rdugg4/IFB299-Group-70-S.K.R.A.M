
class UserVerification(object):
    def LoggedIn(request):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def CustomerLoggedIn(request):
        if request.user.is_authenticated and request.user.groups.filter(name='customer_group').exists():
            return True
        else:
            return False

    def LoggedInID(request):
        if CustomerLoggedIn(request):
            userProfile = Profile.objects.get(user = request.user)
            return userProfile.customerid_id
        else:
            return 0

    def BoardMemberLoggedIn(request):
        if request.user.is_authenticated and request.user.groups.filter(name='boardMember_group').exists():
            return True
        else:
            return False

    def StaffLoggedIn(request):
        if request.user.is_authenticated and (request.user.groups.filter(name='staff_group').exists() or
            request.user.groups.filter(name='boardMember_group').exists()):
            return True
        else:
            return False
