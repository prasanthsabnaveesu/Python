'''
- - - -1
- - - 2 2
- - 3 3 3
- 4 4 4 4
5 5 5 5 5
'''
o=4
f=1
for q in range(1,6,1):
    for p in range(o,0,-1):
        print('-',end=' ')
    for i in range(1,q+1,1):
        print(f,end=' ')
    print()
    f+=1
    o-=1
