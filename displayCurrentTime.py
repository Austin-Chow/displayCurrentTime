#Display current Eastern Standard Time(EST)
import time

#Obtain total number of seconds elapsed since 00:00:00 on January 1, 1970 GMT
currentTime = int(time.time() - 14400) #GMT is 4 hours ahead of EST

#Obtain total number of seconds
seconds = str(currentTime % 60)

#Obtain total number of minutes
minutes = str((currentTime // 60) % 60)

#Obtain total number of hours
hours = str((currentTime // 3600) % 12)
militaryHours = str((currentTime // 3600) % 24)

#Format display time
if int(hours) == 0:
    hours = 12
elif int(hours) < 10:
    hours = "0" + hours

if int(minutes) == 0:
    minutes = 00
elif int(minutes) < 10:
    minutes = "0" + minutes

if int(seconds) == 0:
    seconds = 00
elif int(seconds) < 10:
    seconds = "0" + seconds

#Print current time
if int(militaryHours) >= 12: #Determines AM or PM
    print("The current time is", hours,":",minutes,":", seconds,"PM EST.")
    print("The current time is", militaryHours, ":", minutes, ":", seconds, "PM EST.")
else:
    print("The current time is", hours, ":", minutes, ":", seconds, "AM EST.")
    print("The current time is", militaryHours, ":", minutes, ":", seconds, "AM EST.")