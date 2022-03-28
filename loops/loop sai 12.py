'''
1 2 3
6 5 4
7 8 9
'''

f=1
for x in range(1,4,1):
    if x==2:
        
        for d in range(1,4,1):
            print(f,end=' ')
            f-=1
        f+=4
        print()    
    else:
        for g in range(1,4,1):
            print(f,end=' ')
            f+=1
        print()
        
        f+=2   
