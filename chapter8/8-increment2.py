def increment(time, seconds):
    time.seconds = time.seconds + seconds
    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
        
    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours +1

