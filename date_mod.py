from datetime import date, time

dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]

print(min(dates))
print(max(dates))
print(*sorted(dates))


