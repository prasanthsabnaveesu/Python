'''
****
* *
* *
* *
* *
* *
****
'''
for c in range(1,8,1):
    if c==1 or c==7:
        for h in range(1,5,1):
            print('*',end=' ')
    else:   
        for p in range(1,3,1):
            print('*-',end=' ')
    print()
