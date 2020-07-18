"""
    4. count
"""
# Count number of occurrences of 'RED'
L = ['RED','PURPLE', 'ORANGE', 'RED']
print(L.count('RED'))
# Prints 2

# Count number of occurrences of number '9'
L1 = [2,9,7,9,2,3,4,9]
print(L1.count(9))
# Prints 3

# Count occurrences of all the unique items
L2 = ['A','C','L','C','M']
from collections import Counter
print(Counter(L2))
# Prints Counter({'C': 2, 'A': 1, 'L': 1, 'M': 1})