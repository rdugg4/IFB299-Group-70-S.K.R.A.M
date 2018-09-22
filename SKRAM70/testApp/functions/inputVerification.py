# Create the input verification class a class which helps verify data is of
# the correct form before using
class inputVerification(object):
    # Define the initialisation of an object of the input verification class
    def __init__(self, request):
        """Initialise and object of the inputVerification class...
        This initialisation inputs view request into the object allowing...
        it to be referenced thoughout the objects functions
        """
        self.request = request

    # This function is used in multiple locations to confirm a string is in the
    # get request and that it is of the correct form when it is
    def checkFormGET(self, string, type):
        """Checks if a given string is in the request and is set to a value....
        Depending on the type input it checks if value related to the...
        string in the request is of the correct form for the type input
        """
        returnedValue = self.checkExistance(string)
        if type == 'date' and returnedValue:
            returnedValue = self.isdate(string)
        if type == 'num' and returnedValue:
            returnedValue = self.isint(self.request.GET[string])
        return returnedValue

    # This function is used privately within the class
    def checkExistance(self, string):
        """Checks if a given string is in the resquest and is set to a value
        """
        if (string in self.request.GET) and (self.request.GET[string]):
            return True
        else:
            return False

    # This function is used privately within the class
    def isdate(self, string):
        """Checks if a given value in the request is in the correct format...
        for a date
        """
        try:
            if (self.isint(self.request.GET[string][0:4])) and (self.isint(self.request.GET[string][5:7])) and (self.isint(self.request.GET[string][8:10])):
                return True
            else:
                return False
        except ValueError:
            return False

    # This function is used privately within the class
    def isint(self, value):
        """Checks if a given value is of type int and returns True if it is...
        the case otherwise it returns false
        """
        try:
            int(value)
            return True
        except ValueError:
            return False
