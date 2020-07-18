L = ['PREET', 'HARMAN', 'MANPREET','KAMAL']
x = L.pop()
print(L)
# Prints ['PREET', 'HARMAN', 'MANPREET']

# removed item
print(x)
# Prints KAMAL

del L[0]
print(L)
# Prints ['HARMAN', 'MANPREET']

L.remove('HARMAN')
print(L)
# Prints ['MANPREET']

# L.remove('ppp')
# ValueError: list.remove(x): x not in list

#remove multiple items
L1 = ['R', 'O', 'C', 'K', 'S']
del L1[1:4]
print(L1)
# Prints ['R', 'S']

L1.clear()
print(L1)
# Delete all elements
