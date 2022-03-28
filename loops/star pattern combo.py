'''* *  *
  *  *
     *
     *
  *  *
* * *
'''d=3
l=2
w=3
for x in range(1,4,1):
    for t in range(w,3,-1):
        print('-',end=' ')
    for k in range(d,0,-1):
        print('*',end=' ')
    print()
    d-=1
    w+=1
for v in range(1,4,1):
    for u in range(l,0,-1): 
        print('-',end=' ')
    for p in range(1,v+1,1):
        print('*',end=' ')
    print()
    l-=1
    
