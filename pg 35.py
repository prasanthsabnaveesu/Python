x=int(input('enter no:1'))
y=int(input('enter no:2'))
z=int(input('enter no:3'))

if x==y==z:
    print('eqi')
elif (x==y or x==z) or (y==x or y==z)or (z==x or z==y) :
    print(' iso')
else:
    print('scalene')
    
