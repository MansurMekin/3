from datetime import datetime, timedelta

def choose_plural(amount, *args):
    for el in args:
        if amount % 100 in range(11, 21):
            return f'{amount} {el[2]}'
        elif amount % 10 == 1:
            return f'{amount} {el[0]}'
        elif amount % 10 in range(2, 5):
            return f'{amount} {el[1]}'
        else:
            return f'{amount} {el[2]}'

my_minute = ('минута', 'минуты', 'минут')
my_hour = ('час', 'часа', 'часов')
my_days = ('день', 'дня', 'дней')


pattern = '%d.%m.%Y %H:%M'
current_date = datetime.strptime(input(), pattern)
relize_date = datetime.strptime('08.11.2022 12:00', pattern)

last_time = relize_date - current_date
f_minute = choose_plural((last_time.seconds // 60) % 60, my_minute)
f_hour = choose_plural(last_time.seconds // 3600, my_hour)
f_day = choose_plural(last_time.days, my_days)

if current_date >= relize_date:
	print('Курс уже вышел!')
elif last_time.days == 0 and last_time.seconds // 3600 == 0 and (last_time.seconds // 60) % 60 > 0:
	print(f'До выхода курса осталось: {f_minute}')
elif last_time.days == 0 and last_time.seconds // 3600 > 0 and (last_time.seconds // 60) % 60 == 0:
	print(f'До выхода курса осталось: {f_hour}')
elif last_time.days == 0 and last_time.seconds // 3600 > 0 and (last_time.seconds // 60) % 60 > 0:
	print(f'До выхода курса осталось: {f_hour} и {f_minute}')
elif last_time.days > 0 and last_time.seconds // 3600 == 0 and (last_time.seconds // 60) % 60 == 0:
	print(f'До выхода курса осталось: {f_day}')
else:
	print(f'До выхода курса осталось: {f_day} и {f_hour}')
