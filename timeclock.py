import time

#time math for seconds, hours etc
currentTime = time.time()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60 

totalHours = totalMinutes // 60

currentHour = totalHours % 24 

#defining offset for gmt
offset= eval(input("Enter the offset to GMT: "))

#printing answer.
print("Time is : ", currentHour + offset, ":",
      currentMinute, ":", currentSecond, "GMT")