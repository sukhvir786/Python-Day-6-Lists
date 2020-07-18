"""
    8. pop
"""
# Remove 2nd list item
L1 = ['red', 'green', 'blue']
L1.pop(1)
print(L1)
# Prints ['red', 'blue']

# Remove 2nd list item
L2 = ['red', 'green', 'blue']
L2.pop(-2)
print(L2)
# Prints ['red', 'blue']

L3 = ['red', 'green', 'blue']
x = L3.pop(1)
print(L3)
# removed item
print(x)
# Prints green

L4 = ['red', 'green', 'blue']
L4.pop()
print(L4)
# Prints ['red', 'green']