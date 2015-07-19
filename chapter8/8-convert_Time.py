def convertToSeconds(t):
    minutes = t.hours*60 + t.minutes
    seconds = minutes*60 + t.seconds
    return  seconds

def makeTime(seconds):
    time = Time()
    time.hours = seconds // 3600
    time.minutes = (seconds%3600)  // 60
    time.seconds = seconds%60
    return time

def addTime(t1,t2):
    seconds = convertToSeconds(t1) + convertToSeconds(t2)
    return makeTime(seconds)
