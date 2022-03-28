'''
1
3 2
6 5 4
10 9 8 7
'''

s=3
p=0
t=1
for c in range(1,5,1):
    if c==1 :
        print('1',end=' ')
        print()    
    else:
        for l in range(1,c+1,1):
            print(s,end=' ')
            s-=1
        print()
        s=p+5+s
        p+=2
