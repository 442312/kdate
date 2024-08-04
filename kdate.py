#!/usr/bin/env python3

import datetime

year = datetime.datetime.now().year
now = datetime.datetime.now()
dr = datetime.datetime(year, 11, 29, 22, 00, 00)

if (now < dr):
    delta =  1
else:
    delta = 0

year = datetime.datetime.now().year - delta
dr = datetime.datetime(year, 11, 29, 22, 00, 00)

a = now-dr

day = int(a.days) + 1

print(day)
