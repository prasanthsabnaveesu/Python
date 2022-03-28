'''
* - - * - - *
- * - - * - -
- -  * - -
'''
r=3
for a in range(1,4,1):
    for p in range(1,a,1):
        print(' ',end=' ')
    for q in range(r,0,-1):
        print('*  ',end=' ')
    print()
    r-=1
