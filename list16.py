"""
    7. insert
"""

# Insert 'yellow' at 2nd position
L = ['red', 'green', 'blue']
L.insert(1,'yellow')
print(L)
# Prints ['red', 'yellow', 'green', 'blue']

# Insert 'yellow' at 2nd position
L1 = ['red', 'green', 'blue']
L1.insert(-1,'yellow')
print(L1)
# Prints ['red', 'green', 'yellow', 'blue']

L = ['red', 'green', 'blue']
L.insert(10,'yellow')
print(L)
# Prints ['red', 'green', 'blue', 'yellow']