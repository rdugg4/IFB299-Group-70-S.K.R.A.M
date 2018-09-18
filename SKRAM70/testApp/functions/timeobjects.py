import datetime

class timeObject(object):

    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def weekday(self):
        day = int(str(self.date)[6:8])
        month = int(str(self.date)[4:6])
        year = int(str(self.date)[0:4])
        return datetime.datetime(year, month, day).weekday()

class currentTime(timeObject):
    def __init__(self):
        now = datetime.datetime.now()
        if (now.month < 10):
            self.date = int(str(now.year) + "0" + str(now.month) + str(now.day))
        else:
            self.date = int(str(now.year) + str(now.month) + str(now.day))
        timeObject.__init__(self, self.date)

class givenTime(timeObject):
    def __init__(self, givenTime, order):
        self.date = 0
        if order == 'YMD':
            self.date = int(givenTime[0:4] + givenTime[5:7] + givenTime[8:10])
        elif order == 'DMY':
            self.date = int(givenTime[6:10] + givenTime[3:5] + givenTime[0:2])
        timeObject.__init__(self, self.date)
