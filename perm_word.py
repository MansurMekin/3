import itertools

s = list('abcd')

perm_lst = itertools.permutations(s)
print(*perm_lst)
