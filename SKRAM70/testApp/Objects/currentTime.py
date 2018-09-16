from currentTime import timeObject
import datetime

class currentTime(timeObject):
    date = 0
    def __init__():
        now = datetime.datetime.now()
        if (now.month < 10):
            self.date = int(str(now.year) + "0" + str(now.month) + str(now.day))
        else:
            self.date = int(str(now.year) + str(now.month) + str(now.day))
