
'''
- - - -1
- - - 2 3
- - 3 4 5
- 4 5 6 7
5 6 7 8 9 
'''
y=4
c=1
for g in range(1,6,1):
    for q in range(y,0,-1):
        print('-',end=' ')
    for p in range(1,g+1,1):
        print(c,end=' ')
        c+=1
    c=g+1   
    print()
    y-=1
    
