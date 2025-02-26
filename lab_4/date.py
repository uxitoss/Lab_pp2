#Task 1
from datetime import datetime, timedelta

current_date = datetime.now()
subtract_days = datetime.now() - timedelta(days=5)
print("Current date: ", current_date.strftime("%d.%m.%Y"))
print("Date 5 days ago: ", subtract_days.strftime("%d.%m.%Y"))

#Task 2
from datetime import datetime, timedelta

current_date = datetime.now()
yesterday_date = datetime.now() - timedelta(days=1)
tomorrow_date = datetime.now() + timedelta(days=1)

print("Yesterday date: ", yesterday_date.strftime("%d.%m.%Y"))
print("Current date: ", current_date.strftime("%d.%m.%Y"))
print("Tomorrow date: ", tomorrow_date.strftime("%d.%m.%Y"))

#Task 3
import datetime

current_date = datetime.datetime.now()
print("Current date and time: ", current_date.strftime("%d.%m.%Y %H:%M:%S"))

#Task 4
from datetime import datetime

date1 = input("Enter the first date (DD.MM.YYYY HH:MM:SS): ")
date2 = input("Enter the second date (DD.MM.YYYY HH:MM:SS): ")

def difference_in_sec(date1, date2):
    d1 = datetime.strptime(date1, "%d.%m.%Y %H:%M:%S")
    d2 = datetime.strptime(date2, "%d.%m.%Y %H:%M:%S")

    return abs((d2 - d1).total_seconds())

difference = difference_in_sec(date1, date2)
print("Difference in seconds: ", difference)

