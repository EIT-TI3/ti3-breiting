# (c) &{YEAR} Yannic Breiting

import datetime

# S. 47
def days_parsed(a, b):
    d1, m1, y1, = a.split('.')
    d2, m2, y2, = b.split('.')
    output = 0
    d_diff = abs(int(d2) - int(d1))
    d1, m1, y1 = int(d1), int(m1), int(y1)
    d2, m2, y2 = int(d2), int(m2), int(y2)

    for year in range(int(y1), int(y2) + 1):
        if mod(y1 + year, 4) == 0:
            output += 366
        else:
            output += 365

    for month in range(int(m1), int(m2) + 1):
        if m1 == 1:
            output += 29
        if mod(m1 + month, 2) == 0:
            output += 30
        else:
            output += 31

    print(output + d_diff)


def days_parsed_time(a, b):
    time1 = datetime.datetime.fromisoformat(a)
    time2 = datetime.datetime.fromisoformat(b)
    time_res = time1 - time2
    print(abs(time_res))
