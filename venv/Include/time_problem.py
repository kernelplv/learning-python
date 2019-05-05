#Author of this, please stop that
# on Linux without leading zero (%-d)
# on Windows without leading zero (%#d)
# before this %d = 01
# after this %-d = 1

from datetime import datetime, date, time

def date_time(time_now: str) -> str:
    dt = datetime.strptime(time_now, "%d.%m.%Y %H:%M")
    hrs = ''
    mts = ''
    if dt.hour == 1:
        hrs = 'hour'
    else:
        hrs = 'hours'
    if dt.minute == 1:
        mts = 'minute'
    else:
        mts = 'minutes'
    (print(dt.strftime("%#d %B %Y year %#H "+hrs+" %#M "+mts)))
    return dt.strftime("%#d %B %Y year %#H "+hrs+" %#M "+mts)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")