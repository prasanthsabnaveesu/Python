'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1'''
for x in range(5,0,-1):
    for y in range(5,(x-1),-1):
        print(y,end=' ')
    print()    
