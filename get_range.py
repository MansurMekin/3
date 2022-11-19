from datetime import date

def get_date_range(start, end):
    start_ord = start.toordinal()
    delta_days = end.toordinal() - start.toordinal()
    if delta_days < 0:
        return []
    elif start == end:
        return [start]
    else:
        return list(map(lambda x: (date.fromordinal(start_ord + x)) ,list(range(delta_days + 1))))


day1 = date(2021, 10, 4)
day2 = date(2021, 10, 5)
print(get_date_range(day1, day2), sep='\n')
