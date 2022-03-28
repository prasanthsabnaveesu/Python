n=int(input("sds"))
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev+=r
    rev=rev%9
if rev<10:
    print(rev)   
elif rev%9==0:
    print(' 9')
else:
    print(rev)
        
   
'''
r=123%10= 3
n=123//10= 12
r2=12%10=2
n=12//10=1
r=1%10=1
n=1//10=0'''
