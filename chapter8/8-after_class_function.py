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

	def after(self,time2):
		if self.hours > time2.hours: return 1
		if self.hours < time2.hours: return 0
		if self.minutes > time2.minutes: return 1
		if self.minutes > time2.minutes: return 0
		if self.seconds > time2.seconds: return 1
		return 0




t1 = Time()
t1.hours = 9
t1.minutes = 14
t1.seconds = 30
t2 = Time()
t2.hours = 11
t2.minutes = 14
t2.seconds = 30

print(t1.after(t2))
