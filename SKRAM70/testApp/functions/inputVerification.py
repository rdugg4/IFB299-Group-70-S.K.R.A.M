def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def isdate(value):
    try:
        if (isint(value[0:4])) and (isint(value[5:7])) and (isint(value[8:10])):
            return True
        else:
            return False
    except ValueError:
        return False

def checkExistance(request, string):
    if (string in request.GET) and (request.GET[string]):
        return True
    else:
        return False

def checkFormGET(request, string, type):
    returnedValue = checkExistance(request, string)
    if type == 'date':
        returnedValue = returnedValue and isdate(request.GET[string])
    if type == 'num':
        returnedValue = returnedValue and isint(request.GET[string])
    return returnedValue
