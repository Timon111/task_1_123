duration = int(input())
min = 60
hour = 3600
day = 86400

if duration < min:
    sec = duration
    print("duration = "+str(duration)+":"+str(sec)+" сек")
elif duration < hour:
    new_min = duration // min
    new_sec = duration - new_min * min
    print("duration = "+str(duration)+":"+str(new_min)+" мин "+str(new_sec)+" сек")
elif duration < day:
    new_hour = duration // hour
    new_min = (duration - new_hour * hour) // min
    new_sec = duration - new_hour * hour - new_min * min
    print("duration = "+str(duration)+":"+str(new_hour)+" час "+str(new_min)+" мин "+str(new_sec)+" сек")
else:
    new_day = duration // day
    new_hour = (duration - new_day * day) // hour
    new_min = (duration - new_day * day - new_hour * hour) // min
    new_sec = duration - new_day * day - new_hour * hour - new_min * min
    print("duration = "+str(duration)+":"+str(new_day)+" день "+str(new_hour)+" час "+str(new_min)+" мин"+str(new_sec)+" сек")
