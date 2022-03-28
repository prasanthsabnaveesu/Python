i=[1,2,3,3]
o=iter(i)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
try:
    print(next(o))
except StopIteration:
    print('no elements remaining to iterate')
print('----------------------------------------------------------------')    
i=(1,2,3,3)
o=iter(i)
print(next(o))
while True:
    try:
        print(next(o))
    except StopIteration:
    
        print('no more ele found')
        break
print('----------------------------------------------------------------')      
