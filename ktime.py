import datetime

now = datetime.datetime.now()
today  = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
time = datetime.time(22, 00)
today22 = datetime.datetime(today.year, today.month, today.day, time.hour, time.minute)
yesterday22 = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, time.hour, time.minute)

if (now.hour) < 22 :
     delta = now - yesterday22  
else:
     delta = now - today22

sec = delta.total_seconds()

ktime = sec / 86.4

print(int(ktime))