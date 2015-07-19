def addTime(t1, t2):
	sumt = Time()
	sumt.hours = t1.hours + t2.hours
	sumt.minutes = t1.minutes + t2.minutes
	sumt.seconds = t1.seconds + t2.seconds	
	return sumt	
	
def printTime(time):
    print time.hours, ':', time.minutes, ':', time.seconds

start = Time()
start.hours = 9
start.minutes = 45
start.seconds = 5
duration = Time()
duration.hours = 1
duration.minutes = 35
duration.seconds = 10
done = addTime(start,duration)
printTime done

