'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
for a in range(1,8,1):
    s=1
    for g in range(7,a-1,-1): #5, 5>4,3,2
        print(s,end=' ')
        s+=1
    print()    
