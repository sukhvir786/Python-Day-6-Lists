"""
    9. Remove
"""

# Remove 'green'
L = ['red', 'green', 'blue']
L.remove('green')
print(L)
# Prints ['red', 'blue']

# Remove item from the nested list
L = ['red', 'green', [1, 2, 3]]
L.remove([1, 2, 3])
print(L)
# Prints ['red', 'green']

L = ['red', 'green', 'blue', 'red', 'red']
L.remove('red')
print(L)
# Prints ['green', 'blue', 'red', 'red']

# list comprehension
L = ['red', 'green', 'blue', 'red', 'red']
L = [x for x in L if x is not 'red']
print(L)
# Prints ['green', 'blue']

# lambda expression
L = ['red', 'green', 'blue', 'red', 'red']
L = list(filter(lambda x: x is not 'red', L))
print(L)
# Prints ['green', 'blue']