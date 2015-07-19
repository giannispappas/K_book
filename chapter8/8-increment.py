def increment(time, seconds):
    time.seconds = time.seconds + seconds
    if time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
    if time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours +1

