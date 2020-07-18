#add items to list values
L = ['gray','red','pink']
L.append('blue')
print(L)
# Prints ['gray', 'red', 'pink', 'blue']

#combine list
L1 = ['RED', 'BLUE', 'GREEN']
#L1.extend([1,2,3])
L1.extend('yellow')
print(L1)
# Prints ['RED', 'BLUE', 'GREEN', 1, 2, 3]
# Addition using +
print(L+L1)
