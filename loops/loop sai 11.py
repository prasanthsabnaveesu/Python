'''
1  2   3        
6  5   4
7  8    9
12 11 10
13 14 15
18 17 16

'''

f=1
for x in range(1,4,1):
    
    for y in range(1,4,1):
        
        print(f,end=' ')
        f+=1
    f+=2
    print()
    for z in range(1,4,1):
        print(f,end=' ')
        f=f-1
    f+=4 
    print()    
