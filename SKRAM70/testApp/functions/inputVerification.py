class inputVerification(object):
    def __init__(self, request):
        self.request = request

    def checkFormGET(self, string, type):
        returnedValue = self.checkExistance(string)
        if type == 'date' and returnedValue:
            returnedValue = self.isdate(string)
        if type == 'num' and returnedValue:
            returnedValue = self.isint(self.request.GET[string])
        return returnedValue

    def checkExistance(self, string):
        if (string in self.request.GET) and (self.request.GET[string]):
            return True
        else:
            return False

    def isdate(self, string):
        try:
            if (self.isint(self.request.GET[string][0:4])) and (self.isint(self.request.GET[string][5:7])) and (self.isint(self.request.GET[string][8:10])):
                return True
            else:
                return False
        except ValueError:
            return False

    def isint(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
