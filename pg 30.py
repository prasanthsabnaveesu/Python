'''
* * * * * * * 
            * 
          * 
        * 
      * 
    * 
* * * * * * *
''' 
w=6
for d in range(1,8,1):
    if d==1 or d==7:
        for x in range(1,8,1):
            print('*',end=' ')
        print()
    else:
        for p in range(w,0,-1):
            print(' ',end=' ')
        for f in range(1,2,1):
            print('*',end=' ')
        print()
        w-=1
