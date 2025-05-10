#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
dr = datetime.datetime(1976, 11, 29, 22, 00, 00)

delta = now-dr

olymp = int(delta.days) / 1461

print(round(olymp, 2))

