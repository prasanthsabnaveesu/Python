'''
* - * - *
- * - * -
- - * - -
- * - * -
* - * - *
'''
h=1
k=2
for u in range(1,4,1):
    for a in range(k,2,1):
        print(' ',end=' ')
    for b in range(h,4,1):
        print('* ',end=' ')
    print()
    h+=1
    k-=1
i=1
d=2
for u in range(1,3,1):
    for a in range(d,1,-1): 
        print(' ',end=' ')
    for b in range(i,3,1):
        print('* ',end=' ')
    print()
    i-=1
    d-=1
