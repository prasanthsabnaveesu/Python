'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''
o='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'

r=0
h=0
for x in range(1,6,1):
    for y in range(1,x+1,1):
        print(o[r],end=' ')
        r+=1
    r=r+h
    print()

