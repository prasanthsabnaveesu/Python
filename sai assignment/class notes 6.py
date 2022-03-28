'''
- - - - *
- - - * *
- -  * * *
- * * * * *
* * * * * *
'''
s=4
p=5

for k in  range(1,6,1):
    for l in  range(s,0,-1):
        print('-',end=' ')
    for z in range(p,6,1):
        print('*',end=' ')
    print()
    s-=1
    p-=1
