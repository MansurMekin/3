from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
res = {}

my_res = {}
your_res = {}
current_date = datetime.strptime(input(), pattern)
my_year = current_date.year

for i in range(int(input())):
	name, birthday = input().rsplit(' ', 1)
	res.setdefault(name, datetime.strptime(birthday, pattern))


# print(res)

for k, v in res.items():
	if current_date.month == 12:
		if current_date < v.replace(year=my_year + 1) <= current_date + timedelta(days=7):
			my_res.setdefault(k, v)
	else:
		if current_date < v.replace(year=my_year) <= current_date + timedelta(days=7):
			your_res.setdefault(k, v)


# print(my_res)
# print(max(my_res, key=my_res.get))
# print(max(your_res, key=your_res.get))

if your_res:
	print(max(your_res, key=your_res.get))
elif my_res:
	print(max(my_res, key=my_res.get))
else:
	print('Дни рождения не планируются')
