'''
-12
--3
---
'''
t=1
for d in range(1,4,1):
    
    for a in range(1,d+1,1): #1<4
        print('-',end=' ')
    for w in range(d,3,1): #2<3
        print(t,end=' ')
        t+=1
    print()
    
