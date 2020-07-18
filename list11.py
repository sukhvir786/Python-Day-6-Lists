"""
    2. clear
"""
L = ['KOMAL', 'POOJA', 'SAM']
L.clear()
print(L)
# Prints []

L1 = ['R', 'G', 'B']
del L1[:]
print(L1)
# Prints []

L2 = ['MAPLE', 'ROSE',"TULSI"]
L2[:] = []
print(L2)
# Prints []

L = ['Alpha', 'Beta', 'Gamma']
L *= 0
print(L)
# Prints []