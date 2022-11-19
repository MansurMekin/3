def find_all(target, symbol):
    lst = []
    while symbol in target:
        index = target.find(symbol)
        lst.append(index)
        target = target.replace(symbol, '*', 1)
    return lst
        

# считываем данные
s = input('Введите слово ')
char = input('Введите символ ')

# вызываем функцию
print(find_all(s, char))