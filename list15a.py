L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('x'))
# Triggers ValueError: 'x' is not in list

# also within search bound
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',4,7))
# Triggers ValueError: 'c' is not in list