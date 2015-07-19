class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def printTime(self):
        print(str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds))
        
time1 = Time(9,20,10)
time1.printTime()

time2 = Time(9,20)
time2.printTime()

time3 = Time(9)
time3.printTime()

time4 = Time()
time4.printTime()
