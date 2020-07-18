"""
    10. Reverse
"""

L = ['red', 'green', 'blue']
L.reverse()
print(L)
# Prints ['blue', 'green', 'red']

L = [1, 2, 3, 4, 5]
L.reverse()
print(L)
# Prints [5, 4, 3, 2, 1]

L = ['red', 'green', 'blue']
for x in reversed(L):
  print(x)
# blue
# green
# red