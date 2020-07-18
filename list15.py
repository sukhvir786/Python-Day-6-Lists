"""
    6. Index
"""
# Find the index of 'green' in a list
L = ['red', 'green', 'blue', 'yellow']
print(L.index('green'))
# Prints 1

# Find first occurrence of character ‘c’
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c'))
# Prints 2

# Find 'c' starting a position 5
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',5))
# Prints 8

# Find 'c' in between 5 & 10
L = ['a','b','c','d','e','f','a','b','c','d','e','f']
print(L.index('c',5,10))
# Prints 8

L = ['a','b','c','d','e','f','a','b','c','d','e','f']
if 'x' in L:
    print(L.index('x'))