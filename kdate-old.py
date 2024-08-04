#!/usr/bin/env python3
import datetime

x = datetime.datetime.now()

strdate = str(x)

def feb_days(strdate):
    s = strdate.split(" ")
    ldate = s[0].split("-")
    year = int(ldate[0])
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        feb = 29
    else:
        feb = 28
    return(feb) 

jan = 31
feb = feb_days(strdate)
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30
dec = 31

# Добавить условие: если год високосный, то feb=29, иначе - 28

months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

def get_date_int(strdate, months):
    s = strdate.split(" ")
    ldate = s[0].split("-")
    ltime = s[1].split(":")
    month = int(ldate[1])
    day = int(ldate[2])
    time = int(ltime[0])
    if time >= 22:
        days = 1
    else:
        days = 0
    for x in range(month - 1):
        days += months[x]
    days += day
    return(days) 

curr_date = get_date_int(strdate, months)

def f(i):
    if i > 366:
        return "err"
    if i >= 334:
        return i - 334 + 1
    else:
        return(32 + i)

print(f(curr_date))