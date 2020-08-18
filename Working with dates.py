from datetime import datetime, timedelta

today = datetime.now()
print("Today is: " + str(today))
print("Day "+ str(today.day))
print("Month " + str(today.month))
print("Year " + str(today.year))
print("Hour " + str(today.hour))

one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday was " + str(yesterday))

one_week = timedelta(weeks=1)
yesterweek = today - one_week
print("last week was " + str(yesterweek))

birthday = input("Whem is your birthday (dd/mm/yyyy)? ")
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print("Birthday: " + str(birthday_date))