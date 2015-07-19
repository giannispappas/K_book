class Time:
    pass
def printTime(time):
    print(str(time.hours)+':'+str(time.minutes)+':'+str(time.seconds))

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
printTime(currentTime)


class Time:
	def printTime(time):
		print(str(time.hours)+':'+str(time.minutes)+':'+str(time.seconds))
		
		
class Time:
	def printTime(self):
		print(str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds))
		
		