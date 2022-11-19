import requests

t = input('Введите что то ')
ind1 = t.find('h')
ind2 = t.rfind('h')
print(t[:ind1] + t[ind2:ind1:-1] + t[ind2:])


