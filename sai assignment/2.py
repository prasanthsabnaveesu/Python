'''
A 
B B
C CC
D DDD
E EEEE
'''
f= 'a,b,c,d,e'
l=0
for w in range(1,6,1):
    for q in range(1,w+2,1): #1<3 ,2<3
        if q==2:
            print('-',end=' ')
        else:       
            print(f[l],end=' ')
    l+=1
    print()
    
