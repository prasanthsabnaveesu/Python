
#01 '''''''1 2 3 5 8 13 21

a=0
b=1
t=int(input('fvd'))
print(a,b,end=' ')
for x in range(1,t):
     c=a+b
     a=b
     b=c
     if c<=t:
          print(c,end=' ')
          continue
     else:
          break
        
'''f=int(input('starting range '))
t=int(input('end range'))
a=0
b=1
for x in range(f,t):
     c=a+b
     a=b
     b=c
     if c<=t:
          if c>f:
               print(c,end=' ')
               continue
     else:
          break '''

