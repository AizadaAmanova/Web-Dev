import calendar


month, day, year = map(int, input().split())

weekday_index = calendar.weekday(year, month, day)

day_name = calendar.day_name[weekday_index].upper()

print(day_name)