from datetime import date

def saturdays_between_two_dates(start, end):
	if start > end:
		start, end = end, start
	start_day = start.toordinal()
	end_day = end.toordinal()
	delta = end_day - start_day
	what_start = start.isoweekday()
	what_end = end.isoweekday()

	if what_start == what_end and (what_start != 6 or what_end != 6):
		return int(delta / 7)
	elif what_start == 6 or what_end == 6:
		return int(delta // 7) + 1
	else:
		return int(delta // 7) 
	

	
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))

