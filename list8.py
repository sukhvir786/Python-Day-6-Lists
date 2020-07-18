#list replication
L = ['VIOLET']
L = L * 3
print(L)
# Prints ['VIOLET', 'VIOLET', 'VIOLET']
print(len(L))

if 'VIOLET' in L:
    print('The color is Present in List')

for i in L:
    print(i)
    
L1 = [2,3,1,4,5,6]
for i in L1:
    print(i*2,end=' ')
    
    