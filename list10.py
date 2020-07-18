"""
    1. append
"""
# Append 'POOJA'
L = ['RAMAN','KOMAL','HARMAN']
L.append('POOJA')
print(L)
# Prints ['RAMAN', 'KOMAL', 'HARMAN', 'POOJA']

# Append list to a list
L1 = ['R', 'S', 'T']
L1.append([12,51,34])
print(L1)
# Prints ['R', 'S', 'T', [12, 51, 34]]

# Append tuple to a list
L2 = ['Q', 'R', 'GREEN']
L2.append((1,2,3))
print(L2)
# Prints ['Q', 'R', 'GREEN', (1, 2, 3)]

#append and extend
L1 = ['red', 'green']
L1.append('blue')
print(L1)
# Prints ['red', 'green', 'blue']

L2 = ['red', 'green']
L2.extend('blue')
print(L2)
# Prints ['red', 'green', 'b', 'l', 'u', 'e']