
'''
- -  - - *
- - -  *  * 
- - *  *  *
- * * * *
* * * *
'''
b=4

for f in range(1,6,1):
    for y in range(b,0,-1):
        print('',end=' ')
    for u in range(1,f+1,1):
        print('* ',end=' ')
    print()    
    b-=1
