import time

print("Life stats")
time.sleep(2)
yearsAlive = int(input("How old are you? "))
daysAlive = yearsAlive * 365
time.sleep(2)
print("You have been alive for", daysAlive,"days.")
hoursAlive = daysAlive * 24
time.sleep(2)
print("You have been alive for", hoursAlive,"hours.")
minutesAlive = hoursAlive * 60
time.sleep(2)
print("You have been alive for", minutesAlive,"minutes.")
secondsAlive = minutesAlive * 60
time.sleep(2)
print("You have been alive for", secondsAlive,"seconds.")
