#!/usr/bin/env python3
import datetime
x = datetime.datetime.now()

strdate = str(x)
jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
octb = 31
nov = 30
dec = 31
months = [jan, feb, mar, apr, may, jun, jul, aug, sep, octb, nov, dec]
def get_date_int(strdate, months):
    s = strdate.split(" ")
    ldate = s[0].split("-")
    month = int(ldate[1])
    day = int(ldate[2])
    days = 0
    for x in range(month - 1):
        days += months[x]
    days += day
    return(days)
curr_date = get_date_int(strdate, months)
def f(i):
    if i > 365:
        return "err"
    if i >= 334:
        return i - 334 + 1
    else:
        return(32 + i)

print(f(curr_date))
