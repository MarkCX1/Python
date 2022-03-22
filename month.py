#importing math modules
import math

#inputs asking for year,month, and day
year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day = int(input("Enter the day of the month: 1-31: "))
century = math.floor(year / 100)
yearOfCentury = year % 100


if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1


h = (day + math.floor(26 * (month + 1) / 10) + yearOfCentury + math.floor(yearOfCentury / 4) +
     math.floor(century / 4) + 5 * century) % 7

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
elif h == 6:
    print("Day of the week is Friday")