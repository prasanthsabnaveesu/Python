print('enter no from 1 to 9')

for x in range(1,10):
    n= int(input('no'))
    if n!=5:
        print('try again')
        continue
    else:
        print('well')
        break
