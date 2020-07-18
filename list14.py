"""
    5. extend
"""
# Add multiple items to a list
L = ['RED', 'YELLOW', 'GREEN']
L.extend([1,2,3])
print(L)
# Prints ['RED', 'YELLOW', 'GREEN', 1, 2, 3]

# Add tuple items to a list
L1 = ['R', 'P', 'G']
L1.extend((1,2,3))
print(L1)
# Prints ['R', 'P', 'G', 1, 2, 3]

# Add set items to a list
L3 = ['red', 'green', 'blue']
L3.extend({1,2,3})
print(L3)
# Prints ['red', 'green', 'blue', 1, 2, 3]