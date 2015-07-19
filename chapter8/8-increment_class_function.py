class Time:
	def printTime(self):
		print(str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds))
	
	def increment(self, seconds):
		self.seconds = self.seconds + seconds
		while self.seconds >= 60:
			self.seconds = self.seconds - 60
			self.minutes = self.minutes + 1
			
		while self.minutes >= 60:
			self.minutes = self.minutes - 60
			self.hours = self.hours +1

	
		
currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
currentTime.increment(100)
currentTime.printTime()
