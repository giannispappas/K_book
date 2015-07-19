def addTime(t1, t2):
	sumt = Time()
	sumt.hours = t1.hours + t2.hours
	sumt.minutes = t1.minutes + t2.minutes
	sumt.seconds = t1.seconds + t2.seconds
	
	if sumt.seconds >=60:
		sumt.seconds = sumt.seconds - 60
		sumt.minutes = sumt.minutes + 1
		
	if sumt.minutes >=60:
		sumt.minutes = sumt.minutes -60
		sumt.hours = sumt.hours +1
		
	
	return sumt
	
	
	