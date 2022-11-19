import json


d = {}
lst = []
st = []
with open('people.json', encoding='utf-8') as file:
    data = json.load(file)
    for el in data:
        for k in el:
            lst.append(k)
lst = list(set(lst))
for el in lst:
    d.setdefault(el)

for el in data:
    x = d | el
    st.append(x)

with open('updated_people.json', 'w', encoding='utf-8') as file:
    json.dump(st, file, indent=3)
